angular.module('securemail', ['ngRoute', 'ngResource'])

  .factory('SecureMail', function($resource) {
    var SecureMail = $resource(':protocol//:server/:a/:b', {
      protocol: 'http:',
      server: '86.45.70.108:8080'
    });

    return SecureMail;
  })


  .config(function($routeProvider) {
    $routeProvider
    .when('/', {
      controller: 'RegisterCtrl',
      templateUrl: 'signin.html'
    })
      .when('/register', {
        controller: 'RegisterCtrl',
        templateUrl: 'signin.html'
      })
      .otherwise({
        redirectTo: '/'
      });
  })

  .config(['$locationProvider', function($locationProvider) {
    $locationProvider.hashPrefix('');
  }])

  .controller('RegisterCtrl', function($scope, SecureMail) {

    // $scope.requestInboxClick = function(){
    //   $http.get('http://86.45.70.108:8080/{'+$scope.id+'}:{'+$scope.secret+'}').
    //       then(function(response) {
    //           $scope.response = response.data;
    //           window.alert("Inbox: "+$scope.response);
    //       });
    // },

    $scope.Register = function(){
      $scope.RegisterDetails = SecureMail.get({
        a: 'register'
      });
    };
  });
