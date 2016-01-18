var gulp = require('gulp'),
    nodemon = require('gulp-nodemon');

gulp.task('nodemon', function () {
    nodemon({
        script: 'index.js',
        nodeArgs: ['--harmony']
    }).on('restart');
});

gulp.task('default', ['nodemon']);
