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
      var response = Student.query(function () {
        $scope.students = response.results;
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

    $scope.newStudent = function () {
      // create a Student instance and save it through the API
      Student.save($scope.formStudent, function () {
        $scope.resetForm();
        $scope.getStudents();
      });
    };

    $scope.updateStudent = function () {
      // updates student with given data
      Student.update({ id: $scope.formStudent.pk }, $scope.formStudent, function () {
        $scope.resetForm();
        $scope.getStudents();
      });
    };

    $scope.save = function () {
      // convert the date formart to the one expected for the API
      var date = $scope.formStudent.date_of_birth;
      $scope.formStudent.date_of_birth = $scope.formatDate(date);

      // depending of the available 'pk' attr or not, execute the proper action.
      if (!$scope.formStudent.pk) {
        $scope.newStudent();
      } else {
        $scope.updateStudent();
      }
    };

    $scope.remove = function (pk) {
      Student.delete({ id: pk }, function () {
        $scope.getStudents();
      });
    };

    $scope.edit = function (pk) {
      var student = Student.get({ id: pk }, function () {
        student.date_of_birth = new Date(student.date_of_birth + 'T03:00:00');  // hacky way of avoiding timezone offset in UTC-03
        $scope.formStudent = student;
      });
    };

    $scope.getStudents();
  });
