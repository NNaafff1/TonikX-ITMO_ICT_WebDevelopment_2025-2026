import { createRouter, createWebHistory } from 'vue-router';
import Owners from '@/views/Owners.vue';
import OwnerDetail from '@/views/OwnerDetail.vue';
import Login from '@/components/Login.vue';
import Register from '@/components/Register.vue';

const routes = [
  { path: '/', redirect: '/owners' },
  { path: '/owners', component: Owners },
  { path: '/owners/:id', component: OwnerDetail, props: true },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;