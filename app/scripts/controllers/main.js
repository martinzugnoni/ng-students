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
    $scope.students = [];
    $scope.formStudent = {};

    $scope.getStudents = function () {
      var promise = Student.query(function () {
        $scope.students = promise.results;
      });
    }

    $scope.resetForm = function () {
      $scope.formStudent = {};
    }

    $scope.formatDate = function (date) {
      if (date) {
        return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate();
      } else {
        return null;
      }
    };

    $scope.save = function () {
      // convert the date formart to the one expected for the API
      var date = $scope.formStudent.date_of_birth;
      $scope.formStudent.date_of_birth = $scope.formatDate(date);

      // create a Student instance and save it through the API
      var student = new Student($scope.formStudent);
      student.$save();

      // clean the form
      $scope.resetForm();

      // load new list of students
      $scope.getStudents();
    };

    $scope.remove = function (pk) {
      Student.delete({ id: pk }, function () {
        $scope.getStudents();
      });
    };

    $scope.edit = function (pk) {
      alert('Not implemented');
    };

    $scope.getStudents();
  });
