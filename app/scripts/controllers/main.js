'use strict';

/**
 * @ngdoc function
 * @name ngStudentsApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the ngStudentsApp
 */
angular.module('ngStudentsApp')
  .controller('MainCtrl', function ($scope, Student) {
    var students = Student.query(function () {
      $scope.students = students.results;
    });

    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
