'use strict';

/**
 * @ngdoc service
 * @name ngStudentsApp.Student
 * @description
 * # Student
 * Factory in the ngStudentsApp.
 */
angular.module('ngStudentsApp')
  .factory('Student', ['$resource', function ($resource) {
    return $resource('http://localhost:8000/api/students/:id/', {id: '@id'}, {
        update: {method: 'PUT'},
        query: {method: 'GET', isArray: false}
    });
  }]);
