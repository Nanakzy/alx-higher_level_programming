#!/usr/bin/node

const fs = require('fs');

// Get file paths from command line arguments
const [, , sourceFilePath1, sourceFilePath2, destinationFilePath] = process.argv;

// Read contents of source files
fs.readFile(sourceFilePath1, 'utf8', (err1, data1) => {
  if (err1) {
    console.error(`Error reading ${sourceFilePath1}: ${err1}`);
    return;
  }

  fs.readFile(sourceFilePath2, 'utf8', (err2, data2) => {
    if (err2) {
      console.error(`Error reading ${sourceFilePath2}: ${err2}`);
      return;
    }

    // Concatenate contents of both files
    const concatenatedContent = `${data1}${data2}`;

    // Write concatenated content to destination file
    fs.writeFile(destinationFilePath, concatenatedContent, 'utf8', err3 => {
      if (err3) {
        console.error(`Error writing to ${destinationFilePath}: ${err3}`);
        return;
      }
      console.log(`Concatenated files ${sourceFilePath1} and ${sourceFilePath2} successfully to ${destinationFilePath}`);
    });
  });
});
