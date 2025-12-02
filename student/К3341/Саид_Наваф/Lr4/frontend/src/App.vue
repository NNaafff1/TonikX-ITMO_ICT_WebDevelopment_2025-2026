<template>
  <div id="app">
    <nav>
      <router-link to="/owners">Owners</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/register">Register</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default { name: 'App' }
</script>

<style>
nav { padding: 10px; background: #f5f5f5; }
nav a { margin-right: 10px; }
</style>