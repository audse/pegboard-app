
export type RouteData = {
    params: {
        id?:number,
        url?:string,
    }
}

export type Breadcrumb = {
    name?:string,
    path?:string,
    icon?:string,
}

export type Route = {
    name:string,
    path:string,
    component?:object,
    meta?:{
        requiresAuth?:boolean,
        requiresUnauth?:boolean,
        breadcrumb?:(route?:RouteData) => Array<Breadcrumb>|undefined
    }
}