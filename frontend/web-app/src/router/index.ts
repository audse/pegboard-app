import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
// import Home from '../views/Home.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: () => import("../pages/Home.vue"), // Lazy Load
  },

  {
    path: "/about",
    name: "About",
    component: () => import("../pages/About.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
