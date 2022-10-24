import EmberRouter from '@ember/routing/router';
import config from 'dog-api-frontend/config/environment';

export default class Router extends EmberRouter {
  location = config.locationType;
  rootURL = config.bURL;
}

Router.map(function () {
  this.route('home', { path: '/' });
});