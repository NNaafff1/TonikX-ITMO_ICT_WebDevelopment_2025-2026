<template>
  <div>
    <div class="header-row">
      <h1 class="h1">Cars</h1>
      <div>
        <button class="btn" @click="refresh">Refresh</button>
        <button class="btn secondary" @click="createCar">Add car</button>
      </div>
    </div>

    <div class="card">
      <div v-if="loading" style="padding:24px;">
        <LoadingSpinner />
      </div>
      <div v-else>
        <ul class="list">
          <li v-for="c in cars" :key="c.id" class="list-item">
            <div>
              <router-link :to="{ name: 'CarDetail', params: { id: c.id } }">
                <strong>{{ c.vehicle_model?.manufacturer || '' }} {{ c.vehicle_model?.model || '' }}</strong>
              </router-link>
              <div class="small">VIN: {{ c.vin }}</div>
            </div>
            <div style="display:flex; gap:8px; align-items:center;">
              <router-link :to="{ name: 'CarDetail', params: { id: c.id } }" class="small">View</router-link>
            </div>
          </li>
        </ul>

        <EmptyState v-if="cars.length === 0">No cars found.</EmptyState>
      </div>
    </div>
  </div>
</template>

<script>
import api from "@/services/api";
import LoadingSpinner from "@/components/LoadingSpinner.vue";
import EmptyState from "@/components/EmptyState.vue";

export default {
  components: { LoadingSpinner, EmptyState },
  data(){ return { cars: [], loading: true } },
  async created(){ await this.fetch(); },
  methods:{
    async fetch(){
      this.loading = true;
      try {
        const res = await api.get("api/cars/");
        this.cars = res.data.results || res.data;
      } catch(e){ console.error(e); }
      finally{ this.loading = false; }
    },
    refresh(){ this.fetch(); },
    createCar(){ alert('Car creation UI not implemented yet'); }
  }
}
</script>