<template>
  <div class="container">
    <div class="page-title">
      <h1>Владельцы</h1>
      <button class="btn" @click="fetchOwners">Обновить</button>
    </div>

    <div v-if="loading" class="empty">Загрузка...</div>
    <ul v-else class="grid">
      <li v-for="owner in owners" :key="owner.id" class="owner-card card">
        <div class="name">{{ owner.last_name }} {{ owner.first_name }}</div>
        <div class="meta">DOB: {{ owner.date_of_birth || '—' }}</div>
        <router-link class="btn ghost" :to="`/owners/${owner.id}`">Открыть</router-link>
      </li>
    </ul>

    <p v-if="error" class="alert error">{{ error }}</p>
  </div>
</template>

<script>
import api from '@/services/api';

export default {
  name: 'Owners',
  data() {
    return { owners: [], loading: false, error: null };
  },
  created() {
    this.fetchOwners();
  },
  methods: {
    async fetchOwners() {
      this.error = null;
      this.loading = true;
      try {
        const res = await api.get('/api/owners/');
        // Ожидаем список владельцев (может вернуться paging)
        this.owners = res.data.results || res.data;
      } catch (e) {
        this.error = 'Ошибка получения списка владельцев';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>