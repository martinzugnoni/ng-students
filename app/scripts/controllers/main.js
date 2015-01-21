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

    $scope.formStudent = {};

    $scope.reset = function () {
      $scope.formStudent = {};
    }

    $scope.formatDate = function (date) {
      return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate();
    };

    $scope.save = function () {
      // convert the date formart to the one expected for the API
      var date = $scope.formStudent.date_of_birth;
      $scope.formStudent.date_of_birth = $scope.formatDate(date);

      // create a Student instance and save it through the API
      var student = new Student($scope.formStudent);
      student.$save();

      // clean the form
      $scope.reset();
    };

    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
