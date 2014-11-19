// generate random string, number
// save in files and validate them

function randomString(length, chars) {
    var result = '';
    for (var i = length; i > 0; --i) result += chars[Math.round(Math.random() * (chars.length - 1))];
    return result;
}

function fill() {
	var len = Math.floor((Math.random() * 50) + 1);
	var intnum = Math.floor((Math.random() * 10000000000000000) + 1);
	var realnum = Math.floor((Math.random() * 10) + 1);
	var str = randomString(len, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ');
	var str_num = randomString(len, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ');
	var fill = [intnum, realnum, str, str_num];
	return fill.join(', ');
}

var fs = require('fs');

fs.writeFileSync('my_file.txt', '', { overwrite: true }, function (err) {
		if (err) throw err;
		console.log('It\'s saved!');
});

var fileSizeInMegabytes = 0;
var fileSizeInBytes = 0;

// finish when filesize is more than 10 MB
while (fileSizeInMegabytes < 10) {
	var stats = fs.statSync("my_file.txt");
	fileSizeInBytes = stats["size"];
	fileSizeInMegabytes = fileSizeInBytes / 1000000.0;
	// console.log("FileSize:"+fileSizeInBytes);
	var x=fill();
	// console.log(x);

	// Writing the file
	fd = fs.openSync('my_file.txt', 'a')
	fs.writeSync(fd, x)
	fs.closeSync(fd)
}
