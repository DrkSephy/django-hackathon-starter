'use strict';

restApp.controller('steamSalesController', function($scope, steamSalesFactory) {
    $scope.steamSales= {};
    
    $scope.steamSales = steamSalesFactory.get().success(function(data) {
    	$scope.steamSales = data;
    	console.log(data);
    });
});
