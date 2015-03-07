var re = /ab+c/;
var re = new RegExp("ab+c");

 \: 	caracter especial
 ^: 	principio			$: 		fin
 x*: 	0 or more "x"		x+: 	1 or more "x"
 x?: 	0 or 1 "x"
\f:		Matches a form feed (U+000C).
\n:		Matches a line feed (U+000A).
\r:		Matches a carriage return (U+000D).
\D: 	[^0-9].
{n}: 	ocurrences
{n,m}: 	integers range
\b: 	word boundary

exec:	Executes a search for a match in a string. It returns an array of information.
test:	Rests for a match in a string. Returns true or false.
match:  It returns an array of information or null on a mismatch.
search:	Tests for a match. Returns the index of the match, or -1 if fails.
replace:Replaces the matched substring with a replacement substring.


Flags
g	Global search.
i	Case-insensitive search.
m	Multi-line search.
y	Perform a "sticky" search that matches starting at the current position in the target string

var re = new RegExp("d(b+)d", "g"); var myRe = /d(b+)d/g;
var array = re.exec("cdbbdbsbz");
re[0] = re.array = ["dbbd", "bb"]
re.index = 1;
re.input = "cdbbdbsbz";

var re = /(\w+)\s(\w+)/;
var str = "John Smith";
assert "Smith, John" = str.replace(re, "$2, $1") = /(\w+)\s(\w+) \1 \2/

