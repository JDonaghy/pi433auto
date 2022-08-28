<template>
  <div>
    <main>
        <form @submit.prevent="submit">
          Settings:
          GPIO PIN: {{ picodes.gpio }}

          Sets:
          <div v-for="(set, setname) in picodes.sets" :key="set.id">
            |{{ setname }}|
            <div>Protocol: {{ picodes.sets[setname].protocol }}</div>
            PulseLength: {{ picodes.sets[setname].pulselength }}
            <div v-for="(button, index) in picodes.sets[setname].buttons">
              Button {{ index + 1 }}:
              <div v-for="(btype,bname) in picodes.sets[setname].buttons[index]">
                {{bname}}:<input v-model="picodes.sets[setname].buttons[index][bname]"/> 
              </div> 
            </div>
          </div>
            <button type="submit">
                Save
            </button>
        </form>
    </main>

   
  </div>
</template>

<script>
export default {
  data() {
    return {
      picodes: {},
      serverUrl: "http://127.0.0.1:5000"
    };
  },

  methods: {
    async getData() {
      console.log("1")

      try {
        this.axios.get(this.serverUrl).then((response) => {
          console.log(response.data)
          this.picodes = response.data;
        })
        // JSON responses are automatically parsed.

      } catch (error) {
        console.log(error);
      }
    },
    submit() {
      this.axios.post(this.serverUrl+"/codes", this.picodes)
        .then(response => {
          this.picodes = response.data;
        })
      .catch(err => {console.log(JSON.stringify(err))})
    }
  },
  created() {
    this.getData();
    console.log("0")

  },
};
</script>