const path = require('path');
const fs = require('fs');
// const { EleventyRenderPlugin } = require("@11ty/eleventy");
// const pluginRss = require("@11ty/eleventy-plugin-rss");

module.exports = function(eleventyConfig) {
//   eleventyConfig.addPlugin(EleventyRenderPlugin);
//   eleventyConfig.addPassthroughCopy("splide.min.js");
//   eleventyConfig.addPassthroughCopy("splide.min.css");
//   eleventyConfig.addPassthroughCopy("project-slides.css");
//   eleventyConfig.addPassthroughCopy("bundle.css");
//   eleventyConfig.addPassthroughCopy({ "favicon.png": "/" });
  eleventyConfig.addPassthroughCopy("src/assets");
//   eleventyConfig.addGlobalData("myStatic", "static");
//   // https://www.stefanjudis.com/snippets/how-to-display-the-build-date-in-eleventy/
//   eleventyConfig.addGlobalData('timestamp', () => {
//     let now = new Date();
//     return new Intl.DateTimeFormat(
//       'en-US', { dateStyle: 'full', timeStyle: 'long' }
//     ).format(now);
//   });
  eleventyConfig.addCollection("assets", function(collectionApi) {
      let assetsDir = path.join(__dirname, 'src/assets', 'perso/midi');
      let assets = fs.readdirSync(assetsDir);

      // maybe actually
      return assets;
    });

  return {
    dir: {
      input: "src",
      layouts: "_layouts",
      output: "docs"
    }
  }
};