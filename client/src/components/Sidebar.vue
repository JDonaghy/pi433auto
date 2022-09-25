<template>
    <div class="vh-100" >
        <ul class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start" id="menu">
            <li class="nav-item px-2 w-100" v-for="menuItem in menuItems" :menuItem="menuItem" :key="menuItem._id">
                <a href="#" class="nav-link align-middle px-0" @click="$emit('selectitem', menuItem)" :class="{ 'bg-secondary': menuItem.selected }">
                    <i class="fs-4 bi-house"></i> <span class="ms-1 d-none d-sm-inline">{{menuItem.text}}</span>
                </a>
                <Sidebar v-if="menuItem.childItems" :menuItems="menuItem.childItems" @selectitem="selectitem"></Sidebar>
            </li>
        </ul>
    </div>
</template>


<script>
export default {
    name: 'Sidebar',
    props: ['menuItems'],
    methods: {
        selectitem: function (item) {
            this.$emit('selectitem', item)
        }
    }
}
</script>