<template>
    <div>
        Hello
    </div>
</template>

<script setup>
export default {
  data() {
    return {
      posts: [],
    };
  },

  methods: {
    async getData() {
      try {
        const response = await this.$http.get(
          "http://127.0.0.1:5000"
        );
        // JSON responses are automatically parsed.
        this.pi = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>