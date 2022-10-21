<template>
  <div>
    <main>
      <form @submit.prevent="submit">
        <div class="form-group d-flex flex-row p-2"
          v-for="(btype, bname) in picodes.sets[setname].buttons[currentButtonIndex]" :key="picodes.sets[setname].buttons[currentButtonIndex].id">
          <label class="p-2" for="pwd">{{ bname }}:</label>
          <input class="p-2" type="input" v-model="picodes.sets[setname].buttons[currentButtonIndex][bname]" />
          <div class="btn-group" role="group">
            <button class="btn btn-sm btn-secondary" @click="openLearnDialog(bname)">Learn...</button>
            <button class="btn btn-sm btn-secondary" @click="firecode(bname)">Test</button>
            <button class="btn btn-sm btn-secondary" @click="emitty(bname)">Schedule...</button>
          </div>
        </div>
        <button class="btn btn-primary" type="submit">
          Save
        </button>
      </form>
    </main>
  </div>
</template>

<script>
import LearnCodeDialog from './LearnCode.vue'
import { createConfirmDialog } from 'vuejs-confirm-dialog'
import { ref } from 'vue'
const currentButtonName = ref("")


export default {
  props: ['picodes', 'setname', 'currentButtonIndex', 'onNewcode'],
  methods: {
    openLearnDialog(bname) {
      currentButtonName.value = bname
      this.dialogResult.reveal()
    },
    firecode(bname) {
      const code = this.picodes.sets[this.setname].buttons[this.currentButtonIndex][bname].toString();
      return this.axios({
        url: `http://127.0.0.1:5000/firecode?code=${code}`,
        method: 'GET',
      }).then(({ data }) => {
        console.log(`code fired ${code}`)
      });
    }
  },
  data() {
    return {
      currentButtonName: "",
      dialogResult: {}
    }
  },
  beforeMount () {
    this.dialogResult = createConfirmDialog(LearnCodeDialog )

    this.dialogResult.onConfirm((e) => {
        console.log(`Confirmed! ${JSON.stringify(e)}`)
        this.$emit('newcode',  {code: e.code.code, bname: currentButtonName.value})
    });
    this.dialogResult.onCancel(() => {
      console.log('Canceled!')
    });
  }
};
</script>

