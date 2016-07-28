var gulp = require('gulp'),
    sass = require('gulp-sass'),
    uglify = require('gulp-uglify'),
    concat = require('gulp-concat'),
    newer = require('gulp-newer'),
    sourcemaps = require('gulp-sourcemaps'),
    plumber = require('gulp-plumber'),
    notify = require("gulp-notify"),
    environments = require('gulp-environments'),
    gutil = require('gulp-util'),
    runSequence = require('run-sequence');


// Environments

var development = environments.development;
var production = environments.production;


// Paths

var images = ['assets/img/**/*'];
var scripts = ['assets/js/**/*.js'];
var styles = ['assets/scss/app.scss'];

var out = {
    js: 'assets/_build/js/',
    css: 'assets/_build/css/',
    img: 'assets/_build/img/',
};


// Tasks

gulp.task('scripts', function() {
    gulp.src(scripts)
        .pipe(development(plumber({errorHandler: notify.onError("Error: <%= error.message %>")})))
        .pipe(production(uglify()))
        .pipe(concat('app.js'))
        .pipe(gulp.dest(out.js));
});

gulp.task('styles', function() {
    gulp.src(styles)
        .pipe(development(plumber({errorHandler: notify.onError("Error: <%= error.message %>")})))
        .pipe(development(sourcemaps.init()))
        .pipe(sass({outputStyle: production() ? 'compressed' : 'nested'}).on('error', sass.logError))
        .pipe(development(sourcemaps.write()))
        .pipe(concat('app.css'))
        .pipe(gulp.dest(out.css));
});

gulp.task('images', function() {
    return gulp.src(images)
        .pipe(newer(out.img))
        .pipe(gulp.dest(out.img));
});


// I'm watching you!

gulp.task('watch', function() {
    gulp.watch(['assets/scss/**/*.scss'], ['styles']);
    gulp.watch(scripts, ['scripts']);
    gulp.watch(images, ['images']);
});


// Default

gulp.task('default', ['styles', 'scripts', 'images', 'watch']);


// Build (with proper error exit code)

gulp.task('build', function(cb) {
    environments.current(production);
    runSequence(['styles', 'scripts', 'images']);
});
