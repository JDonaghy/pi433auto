
<template>
    <div class="container-fluid">
        <div class="row flex-nowrap">
            <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0 bg-dark">
                <Sidebar :menuItems="menuItems" @selectitem="selectitem"></Sidebar>
            </div>
            <div class="col py-3" v-if="menuItems.length > 0">
                <SetSettings v-if="this.viewtype === 'set'" :picodes="picodes"
                    :setname="menuItems[currentSetIndex].text" />
                <PiCodes v-else :picodes="picodes" :setname="menuItems[currentSetIndex].text"
                    :currentButtonIndex="currentButtonIndex" v-on:newcode="setnewcode"/>
            </div>

        </div>
    </div>

</template>
  

<script>
import PiCodes from './PiCodes.vue'
import SetSettings from './SetSettings.vue'
import Sidebar from './Sidebar.vue'

export default {
    components: {
        Sidebar,
        PiCodes,
        SetSettings
    },
    data() {
        return {
            menuItems: [],
            picodes: {},
            serverUrl: "http://127.0.0.1:5000",
            loading: true,
            errors: false,
            currentSetIndex: 0,
            currentButtonIndex: 0,
            viewtype: "button",
            menu: [
                {
                    header: 'Button Sets',
                    hiddenOnCollapse: true
                },
                {
                    href: '/',
                    title: 'Dashboard',
                    icon: 'fa fa-user'
                },
                {
                    href: '/charts',
                    title: 'Charts',
                    icon: 'fa fa-chart-area',
                    child: [
                        {
                            href: '/charts/sublink',
                            title: 'Sub Link'
                        }
                    ]
                }
            ]
        }
    },
    methods: {
        setnewcode(codeinfo) {
            debugger
            const setname = this.menuItems[this.currentSetIndex].text
            this.picodes.sets[setname].buttons[this.currentButtonIndex][codeinfo.bname] = codeinfo.code
        },
        async getData() {
            try {
                this.axios.get(this.serverUrl).then((response) => {
                    console.log(response.data)
                    this.picodes = response.data;
                    let setIndex = 0
                    for (const setprop in this.picodes.sets) {
                        const childItems = []
                        for (let i = 0; i < this.picodes.sets[setprop].buttons.length; i++) {
                            childItems.push({
                                text: "button " + (i + 1), type: "button", index: i, parentIndex: this.menuItems.length, selected: false
                            })
                        }
                        this.menuItems.push({
                            text: setprop, type: "set", childItems: childItems, selected: false, index: setIndex
                        })
                        setIndex++
                    }
                    this.currentSetIndex = 0
                })
                // JSON responses are automatically parsed.
                this.loading = false

            } catch (error) {
                console.log(error);
                this.errors = true
            }
        },
        selectitem(item) {
            this.viewtype = item.type
            for (let i in this.menuItems) {
                this.menuItems[i].selected = false
                for (let j in this.menuItems[i].childItems) {
                    this.menuItems[i].childItems[j].selected = false
                }
            }
            if (item.type !== "set") {
                this.currentSetIndex = item.parentIndex
                this.currentButtonIndex = item.index
                this.menuItems[this.currentSetIndex].childItems[this.currentButtonIndex].selected = true
            } else {
                item.selected = true
            }

        }
    },
    created() {
        this.getData();
    },
}
</script>