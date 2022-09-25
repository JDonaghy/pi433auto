<template>
  <div>
    <main>
      <form @submit.prevent="submit">
        <div class="form-group d-flex flex-row p-2"
          v-for="(btype, bname) in picodes.sets[setname].buttons[currentButtonIndex]">
          <label class="p-2" for="pwd">{{ bname }}:</label>
          <input class="p-2" type="input" v-model="picodes.sets[setname].buttons[currentButtonIndex][bname]" />
          <div class="btn-group" role="group">
            <button class="btn btn-sm btn-secondary">Learn...</button>
            <button class="btn btn-sm btn-secondary">Schedule...</button>
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
export default {
  props: ['picodes', 'setname', 'currentButtonIndex'],
};
</script>