// 1. Include gulp
var gulp = require('gulp');

// 2. Include any plugins you might need.
var process = require('child_process');
var install = require("gulp-install");
// 3. Write out the tasks 

gulp.task('bowerinstall',function(){
	console.info('Installing Bower Packages.')
    gulp.src(['./bower.json', './package.json'])
    .pipe(install());
})

gulp.task('djangomigrate', function(){
	var spawn = process.spawn;
	console.info('Doing Django Migrations');
	var PIPE = {stdio: 'inherit'};
	spawn('python',['./hackathon_starter/manage.py','migrate'],PIPE);
});

gulp.task('django', function(){
	var spawn = process.spawn;
	console.info('Starting Django server');
	var PIPE = {stdio: 'inherit'};
	spawn('python',['./hackathon_starter/manage.py','runserver'],PIPE);
});

// 4. Default Task
gulp.task('default',['bowerinstall','django','djangomigrate']);
