module.exports = function (grunt) {
  'use strict';

  // Force use of Unix newlines
  grunt.util.linefeed = '\n';

  RegExp.quote = function (string) {
    return string.replace(/[-\\^$*+?.()|[\]{}]/g, '\\$&');
  };

  var fs = require('fs');
  var path = require('path');

  // Project configuration.
  grunt.initConfig({

    less: {
      compileCore: {
        options: {
          strictMath: true,
          sourceMap: true,
          outputSourceFiles: true,
          sourceMapURL: 'app.css.map',
          sourceMapFilename: 'tweetset/collect/static/css/app.css.map'
        },
        files: {
          'tweetset/collect/static/css/app.css': 'less/bootstrap.less'
        }
      },
      minify: {
        options: {
          cleancss: true,
          report: 'min'
        },
        files: {
          'tweetset/collect/static/css/app.min.css': 'tweetset/collect/static/css/app.css',
        }
      }
    },

    watch: {
      less: {
        files: 'less/*.less',
        tasks: ['less'],
      }
    },      

  });


  // These plugins provide necessary tasks.
  require('load-grunt-tasks')(grunt, {scope: 'devDependencies'});

  grunt.registerTask('build', ['less']);

  grunt.registerTask('default', ['less']);

};
