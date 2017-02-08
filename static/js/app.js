angular.module('Anonymizer', ['ngAnimate', 'ngMaterial', 'ngResource', 'ui.router']);

angular.module('Anonymizer').config(["$resourceProvider", function($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
}]);

angular.module('Anonymizer').config(["$stateProvider", "$urlRouterProvider", function($stateProvider, $urlRouterProvider){
    $urlRouterProvider.when('', '/');
    $stateProvider.state('home', {
	url: '/', params: {onlyJoin:true},
	templateUrl: 'static/views/page1.html', controller: 'HomeC'
    }).state('operator', {
	url: '/operator', params: {onlyStart:true},
	templateUrl: 'static/views/home.html', controller: 'HomeC'
    })
}])

angular.module('Anonymizer').controller('HomeC', ['$scope', function($scope){
    $scope.data = [1,2,3,4,5,6,7]
}]);
