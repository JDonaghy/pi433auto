<template>
  <div class="modal-container">
    <div class="modal-body">
      Codes:
      <div class="scroll">
        <div v-for="row in rows">
          {{row}}
        </div>
      </div>
      <div v-if="gotCode">
        Likely code value is {{bestcode.code}} found {{bestcode.count}} times(s). Press 'Confirm' to use this value.
      </div>
      <div class="modal-action">
        <button class="modal-button" @click="emit('confirm', {code: bestcode, me: this})">Confirm</button>
        <button class="modal-button" @click="emit('cancel')">Cancel</button>
      </div>
    </div>
  </div>
</template>
  
<script setup>

const emit = defineEmits(['confirm', 'cancel', 'setBestCode'])
</script>
  

<script>
function findBestCode(rows) {
  let codes = [];
  for (let row of rows) {
    if (row.includes("pulselength")) {
      const rowItems = row.split(' ')
      const newCode = rowItems[0]
      const found = codes.find(c => c.code === newCode)
      if (found) {
        found.count++
      } else {
        codes.push({ code: newCode, count: 1 })
      }
    }
  }
  const max = codes.reduce(function (prev, current) {
    return (prev.count > current.count) ? prev : current
  })
  return max
}

export default {
  data() {
    return {
      rows: [],
      responseLength: 0,
      bestcode: {},
      gotCode: false
    }
  },
  methods: {
    getDataFromStream(_data) {
      return this.axios({
        url: `http://127.0.0.1:5000/stream`,
        method: 'GET',
        onDownloadProgress: progressEvent => {
          let dataChunk = progressEvent.currentTarget.response;
          let lines = dataChunk.substring(this.responseLength).split("\n")
          this.responseLength = dataChunk.length
          // dataChunk = dataChunk.replaceAll("'", "")
          for (let line of lines) {
            this.rows.push(line)
          }
        }


      }).then(({ data }) => {
        this.bestcode = findBestCode(this.rows);
        this.gotCode = true;
        console.log(`best: ${JSON.stringify(this.bestcode)}`)
        Promise.resolve(data)
      });
    }

  },
  created() {
    this.getDataFromStream();
  }
}

</script>
  
<style>
div.scroll {
  margin: 4px, 4px;
  padding: 4px;
  height: 110px;
  overflow-x: hidden;
  overflow-y: auto;
  text-align: justify;
}

.modal-container {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  height: 100%;
  background-color: #cececeb5;
}

.modal-body {
  background-color: #fff;
  border: 2px solid #74a2cf;
  border-radius: 10px;
  text-align: center;
  padding: 20px 40px;
  max-width: 70vw;
  display: flex;
  flex-direction: column;
}

.modal-action {
  display: flex;
  flex-direction: row;
  gap: 40px;
  justify-content: center;
}

.modal-button {
  cursor: pointer;
  height: 30px;
  padding: 0 25px;
  border: 2px solid #74a2cf;
  border-radius: 5px;
  background-color: #80b2e4;
  color: #fff;
}
</style>