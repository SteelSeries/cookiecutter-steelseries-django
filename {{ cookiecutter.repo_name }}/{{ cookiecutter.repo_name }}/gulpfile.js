var gulp = require('gulp'),
    concat = require('gulp-concat'),
    newer = require('gulp-newer'),
    uglify = require('gulp-uglify'),
    sass = require('gulp-sass'),
    imagemin = require('gulp-imagemin');


// Paths

var images = ['assets/img/**/*'];
var styles = ['assets/scss/app.scss'];
var scripts = ['assets/js/**/*.js'];

var out = {
    dev: 'assets/_build/dev/',
    prod: 'assets/_build/prod/',
    img: 'assets/_build/img/',
};


// Tasks

gulp.task('scripts', function() {
    gulp.src(scripts)
        .pipe(concat('app.js'))
        .pipe(gulp.dest(out.dev));

    gulp.src(scripts)
        .pipe(uglify())
        .pipe(concat('app.js'))
        .pipe(gulp.dest(out.prod));
});

gulp.task('styles', function() {
    gulp.src(styles)
        .pipe(sass({sourceComments: 'map'}))
        .pipe(concat('app.css'))
        .pipe(gulp.dest(out.dev));

    gulp.src(styles)
        .pipe(sass({outputStyle: 'compressed'}))
        .pipe(concat('app.css'))
        .pipe(gulp.dest(out.prod));
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
