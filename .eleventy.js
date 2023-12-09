const path = require('path');
const fs = require('fs');
const glob = require('glob');
// const { EleventyRenderPlugin } = require("@11ty/eleventy");
// const pluginRss = require("@11ty/eleventy-plugin-rss");

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
//   eleventyConfig.addPlugin(EleventyRenderPlugin);
//   eleventyConfig.addPassthroughCopy("splide.min.js");
//   eleventyConfig.addPassthroughCopy("splide.min.css");
//   eleventyConfig.addPassthroughCopy("project-slides.css");
//   eleventyConfig.addPassthroughCopy("bundle.css");
//   eleventyConfig.addPassthroughCopy({ "favicon.png": "/" });
  eleventyConfig.addPassthroughCopy("src/assets");

  // need to add add dependencies for MIDI playback
  // eleventyConfig.addPassthroughCopy("src/assets");
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
    midi_asset_path = 'src/assets/**/midi/*.mid';

    // note: still haven't normalized filenname extensions ...
    midi_assets = await readFilesInSubdirectories(midi_asset_path);

    // mightn want to package these up into objects that contain more metadata for the front-end
    return midi_assets;
  });

  return {
    dir: {
      input: "src",
      layouts: "_layouts",
      output: "docs"
    }
  }
};