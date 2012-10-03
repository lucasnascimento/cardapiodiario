'use strict';

describe('Service: restaurant', function () {

  // load the service's module
  beforeEach(module('layoutApp'));

  // instantiate service
  var restaurant;
  beforeEach(inject(function(_restaurant_) {
    restaurant = _restaurant_;
  }));

  it('should do something', function () {
    expect(!!restaurant).toBe(true);
  });

});
