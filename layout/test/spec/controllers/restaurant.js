'use strict';

describe('Controller: RestaurantCtrl', function() {

  // load the controller's module
  beforeEach(module('layoutApp'));

  var RestaurantCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function($controller) {
    scope = {};
    RestaurantCtrl = $controller('RestaurantCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function() {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
