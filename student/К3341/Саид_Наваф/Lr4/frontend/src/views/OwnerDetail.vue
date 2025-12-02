<template>
  <div>
    <button @click="$router.back()">Назад</button>
    <div v-if="loading">Загрузка...</div>
    <div v-else-if="owner">
      <h2>{{ owner.last_name }} {{ owner.first_name }}</h2>
      <p>Дата рождения: {{ owner.date_of_birth }}</p>

      <div v-if="owner.driver_license">
        <h3>Водительское удостоверение</h3>
        <p>Номер: {{ owner.driver_license.license_number }}</p>
        <p>Дата выдачи: {{ owner.driver_license.issue_date }}</p>
      </div>

      <div v-if="owner.ownerships && owner.ownerships.length">
        <h3>Владения</h3>
        <ul>
          <li v-for="o in owner.ownerships" :key="o.id">
            {{ o.car.make }} {{ o.car.model }} ({{ o.date_start }} — {{ o.date_end || 'по настоящее время' }})
          </li>
        </ul>
      </div>
    </div>
    <p v-else>Владелец не найден</p>
  </div>
</template>

<script>
import api from '@/services/api';

export default {
  name: 'OwnerDetail',
  props: ['id'],
  data() {
    return { owner: null, loading: false, error: null };
  },
  async created() {
    const ownerId = this.$route.params.id;
    this.fetchOwner(ownerId);
  },
  methods: {
    async fetchOwner(id) {
      this.loading = true;
      try {
        const res = await api.get(`/api/owners/${id}/`);
        this.owner = res.data;
      } catch (e) {
        this.error = 'Ошибка получения владельца';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>