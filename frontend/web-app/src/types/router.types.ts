import { RouteLocationNormalizedLoaded } from "vue-router"

type Breadcrumb = {
    name?:string,
    path?:string,
    icon?:string,
}

declare module 'vue-router' {
    interface RouteMeta {
        requiresAuth?:boolean
        requiresNoAuth?:boolean
        breadcrumb:(route?:RouteLocationNormalizedLoaded) => Array<Breadcrumb>
    }
  }