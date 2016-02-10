var gulp = require('gulp'),
    concat = require('gulp-concat'),
    newer = require('gulp-newer'),
    uglify = require('gulp-uglify'),
    sass = require('gulp-sass'),
    sourcemaps = require('gulp-sourcemaps'),
    imagemin = require('gulp-imagemin'),
    plumber = require('gulp-plumber'),
    notify = require("gulp-notify");


// Paths

var images = ['assets/img/**/*'];
var styles = ['assets/scss/app.scss'];
var scripts = ['assets/js/**/*.js'];

var out = {
    js: 'assets/_build/js/',
    css: 'assets/_build/css/',
    img: 'assets/_build/img/',
};


// Tasks

gulp.task('scripts', function() {
    gulp.src(scripts)
        .pipe(plumber({errorHandler: notify.onError("Error: <%= error.message %>")}))
        .pipe(concat('{{ cookiecutter.repo_name }}.js'))
        .pipe(gulp.dest(out.js))
        .pipe(livereload());
});

gulp.task('styles', function() {
    gulp.src(styles)
        .pipe(plumber({errorHandler: notify.onError("Error: <%= error.message %>")}))
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(sourcemaps.write())
        .pipe(concat('{{ cookiecutter.repo_name }}.css'))
        .pipe(gulp.dest(out.css));
});

gulp.task('images', function() {
    return gulp.src(images)
        .pipe(newer(out.img))
        .pipe(imagemin({optimizationLevel: 5}))
        .pipe(gulp.dest(out.img));
});


// I'm watching you!

gulp.task('watch', function() {
    gulp.watch(scripts, ['scripts']);
    gulp.watch(styles, ['styles']);
    gulp.watch(images, ['images']);
});


// Default

gulp.task('default', ['styles', 'scripts', 'images', 'watch']);
