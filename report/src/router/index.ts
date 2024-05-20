import { createRouter, createWebHistory } from 'vue-router'
import DashboardPage from '../views/pages/Dashboard.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: DashboardPage
    },
    {
      path: '/test-report',
      name: 'test-report',
      component: () => import('../views/pages/TestReport.vue')
    },
    {
      path: '/test-case-execute-details',
      name: 'test-case-execute-details',
      component: () => import('../views/pages/TestCaseExecuteDetails.vue')
    }
  ]
})

export default router
