const fs = require('fs');
const archiver = require('archiver');

let output = fs.createWriteStream('./docs/assets/midi.zip');
let archive = archiver('zip', {
    zlib: { level: 9 } // Sets the compression level.
});

// This event listener will tell you when the archive is finalized and the output file descriptor is closed.
output.on('close', function() {
    console.log(archive.pointer() + ' total bytes');
    console.log('Archiver has been finalized and the output file descriptor has closed.');
});

archive.pipe(output);

// Append files from different directories
directories = [
    'src/assets/perso/midi/',
    'src/assets/prairiefrontier/midi/',
    'src/assets/emusic/midi/',
    'src/assets/sankey/midi',
    'src/assets/irishmidifiles/midi',
    'src/assets/aol_israelmidi/midi',
    'src/assets/vietvet/midi',
    'src/assets/laurasmidiheaven/midi',
]
for (let dir of directories)  {
    archive.directory(dir, false)
}

// Finalize the archive (i.e., we are done appending files but streams have to finish yet)
archive.finalize();