var gulp = require('gulp'),
    nodemon = require('gulp-nodemon'),
    mocha = require('gulp-mocha-co'),
    exit = require('gulp-exit');

gulp.task('nodemon', function () {
    nodemon({
        script: 'index.js',
        nodeArgs: ['--harmony']
    }).on('restart');
});

gulp.task('test', function () {
    gulp.src(['test/*.js'])
        .pipe(mocha({
            reporter: 'nyan'
        }))
        .pipe(exit());
});

gulp.task('default', ['nodemon']);
