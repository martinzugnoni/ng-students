'use strict';

/**
 * @ngdoc function
 * @name ngStudentsApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the ngStudentsApp
 */
angular.module('ngStudentsApp')
  .controller('AboutCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
