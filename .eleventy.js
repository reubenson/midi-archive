const path = require('path');
const fs = require('fs');
const glob = require('glob');
const { exec } = require('child_process');

async function readFilesInSubdirectories(pattern) {
  return new Promise((resolve, reject) => {
    glob(pattern, (err, files) => {
      if (err) {
        return reject(err);
      }
      files = files.map(file => {
        return file.replace('src/assets/', '/assets/');
      });
      resolve(files);
    });
  });
}


module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("src/assets");

  // add dependencies for MIDI player
  eleventyConfig.addPassthroughCopy({ "./node_modules/timidity/libtimidity.wasm": "assets/timidity/libtimidity.wasm" });
  eleventyConfig.addPassthroughCopy({ "./node_modules/freepats/Tone_000": "assets/timidity/Tone_000" });
  eleventyConfig.addPassthroughCopy({ "./node_modules/freepats/Drum_000": "assets/timidity/Drum_000" });
//   eleventyConfig.addGlobalData("myStatic", "static");
//   // https://www.stefanjudis.com/snippets/how-to-display-the-build-date-in-eleventy/
//   eleventyConfig.addGlobalData('timestamp', () => {
//     let now = new Date();
//     return new Intl.DateTimeFormat(
//       'en-US', { dateStyle: 'full', timeStyle: 'long' }
//     ).format(now);
//   });
  eleventyConfig.addCollection("midiAssets", async function(collectionApi) {
    const sites_data = require('./sites.json')
    const midi_assets = {};

    // note: still haven't normalized filenname extensions ...
    midi_files = await readFilesInSubdirectories('src/assets/**/midi/*.mid');
    midi_files = midi_files.concat(await readFilesInSubdirectories('src/assets/**/midi/*.MID'));

    midi_files.forEach(file => {
      const site_name = file.split('/')[2];

      midi_assets[site_name] = midi_assets[site_name] || [];
      midi_assets[site_name].push(file);

      sites_data[site_name].midis = sites_data[site_name].midis || [];
      sites_data[site_name].midis.push(file);
    })

    return sites_data;
  });

  eleventyConfig.on('afterBuild', () => {
    console.log('Eleventy has finished building!');

    exec('npm run bundle', (error, stdout, stderr) => {
      if (error) {
        console.error(`exec error: ${error}`);
        return;
      }
      console.log(`stdout: ${stdout}`);
      console.error(`stderr: ${stderr}`);
    });
  });

  return {
    dir: {
      input: "src",
      layouts: "_layouts",
      output: "docs",
      pathPrefix: '/midi-archive/'
      // pathPrefix: isProduction ? `/midi-archive/` : `/`, 
    }
  }
};