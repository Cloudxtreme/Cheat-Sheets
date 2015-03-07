* As a function
{{{
function User (type) {
    this.name = name;
    this.age = "red";
    this.getInfo = getAppleInfo;
}
 
function getAppleInfo() { // mem expensive!
    return this.name + ' ' + this.age;
}

Apple.prototype.getInfo2 = function() {
    return this.name + '-' + this.age;
};

var user = new User('BuFer');
apple.age = 30;
apple.getInfo();
}}}
* As object instance
{{{
var user = {
    name: "BuFer",
    age: 30,
    getInfo: function () {
        return this.name + '-' + this.age;
    }
}
}}}
* Singleton
{{{
var apple = new function() {
    this.name = "BuFer";
    this.age = 30;
    this.getInfo = function () {
        return this.name + '-' + this.age;
    };
}
}}}
