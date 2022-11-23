(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["Category"],{1681:function(t,e,i){},"169a":function(t,e,i){"use strict";i("368e");var s=i("480e"),a=i("4ad4"),o=i("b848"),n=i("75eb"),l=(i("3c93"),i("a9ad")),r=i("7560"),c=i("f2e7"),d=i("58df"),h=Object(d["a"])(l["a"],r["a"],c["a"]).extend({name:"v-overlay",props:{absolute:Boolean,color:{type:String,default:"#212121"},dark:{type:Boolean,default:!0},opacity:{type:[Number,String],default:.46},value:{default:!0},zIndex:{type:[Number,String],default:5}},computed:{__scrim(){const t=this.setBackgroundColor(this.color,{staticClass:"v-overlay__scrim",style:{opacity:this.computedOpacity}});return this.$createElement("div",t)},classes(){return{"v-overlay--absolute":this.absolute,"v-overlay--active":this.isActive,...this.themeClasses}},computedOpacity(){return Number(this.isActive?this.opacity:0)},styles(){return{zIndex:this.zIndex}}},methods:{genContent(){return this.$createElement("div",{staticClass:"v-overlay__content"},this.$slots.default)}},render(t){const e=[this.__scrim];return this.isActive&&e.push(this.genContent()),t("div",{staticClass:"v-overlay",on:this.$listeners,class:this.classes,style:this.styles},e)}}),u=h,m=i("80d2"),v=i("2b0e"),p=v["a"].extend().extend({name:"overlayable",props:{hideOverlay:Boolean,overlayColor:String,overlayOpacity:[Number,String]},data(){return{animationFrame:0,overlay:null}},watch:{hideOverlay(t){this.isActive&&(t?this.removeOverlay():this.genOverlay())}},beforeDestroy(){this.removeOverlay()},methods:{createOverlay(){const t=new u({propsData:{absolute:this.absolute,value:!1,color:this.overlayColor,opacity:this.overlayOpacity}});t.$mount();const e=this.absolute?this.$el.parentNode:document.querySelector("[data-app]");e&&e.insertBefore(t.$el,e.firstChild),this.overlay=t},genOverlay(){if(this.hideScroll(),!this.hideOverlay)return this.overlay||this.createOverlay(),this.animationFrame=requestAnimationFrame(()=>{this.overlay&&(void 0!==this.activeZIndex?this.overlay.zIndex=String(this.activeZIndex-1):this.$el&&(this.overlay.zIndex=Object(m["u"])(this.$el)),this.overlay.value=!0)}),!0},removeOverlay(t=!0){this.overlay&&(Object(m["a"])(this.overlay.$el,"transitionend",()=>{this.overlay&&this.overlay.$el&&this.overlay.$el.parentNode&&!this.overlay.value&&!this.isActive&&(this.overlay.$el.parentNode.removeChild(this.overlay.$el),this.overlay.$destroy(),this.overlay=null)}),cancelAnimationFrame(this.animationFrame),this.overlay.value=!1),t&&this.showScroll()},scrollListener(t){if("key"in t){if(["INPUT","TEXTAREA","SELECT"].includes(t.target.tagName)||t.target.isContentEditable)return;const e=[m["x"].up,m["x"].pageup],i=[m["x"].down,m["x"].pagedown];if(e.includes(t.keyCode))t.deltaY=-1;else{if(!i.includes(t.keyCode))return;t.deltaY=1}}(t.target===this.overlay||"keydown"!==t.type&&t.target===document.body||this.checkPath(t))&&t.preventDefault()},hasScrollbar(t){if(!t||t.nodeType!==Node.ELEMENT_NODE)return!1;const e=window.getComputedStyle(t);return(["auto","scroll"].includes(e.overflowY)||"SELECT"===t.tagName)&&t.scrollHeight>t.clientHeight||["auto","scroll"].includes(e.overflowX)&&t.scrollWidth>t.clientWidth},shouldScroll(t,e){if(t.hasAttribute("data-app"))return!1;const i=e.shiftKey||e.deltaX?"x":"y",s="y"===i?e.deltaY:e.deltaX||e.deltaY;let a,o;"y"===i?(a=0===t.scrollTop,o=t.scrollTop+t.clientHeight===t.scrollHeight):(a=0===t.scrollLeft,o=t.scrollLeft+t.clientWidth===t.scrollWidth);const n=s<0,l=s>0;return!(a||!n)||(!(o||!l)||!(!a&&!o)&&this.shouldScroll(t.parentNode,e))},isInside(t,e){return t===e||null!==t&&t!==document.body&&this.isInside(t.parentNode,e)},checkPath(t){const e=Object(m["g"])(t);if("keydown"===t.type&&e[0]===document.body){const e=this.$refs.dialog,i=window.getSelection().anchorNode;return!(e&&this.hasScrollbar(e)&&this.isInside(i,e))||!this.shouldScroll(e,t)}for(let i=0;i<e.length;i++){const s=e[i];if(s===document)return!0;if(s===document.documentElement)return!0;if(s===this.$refs.content)return!0;if(this.hasScrollbar(s))return!this.shouldScroll(s,t)}return!0},hideScroll(){this.$vuetify.breakpoint.smAndDown?document.documentElement.classList.add("overflow-y-hidden"):(Object(m["b"])(window,"wheel",this.scrollListener,{passive:!1}),window.addEventListener("keydown",this.scrollListener))},showScroll(){document.documentElement.classList.remove("overflow-y-hidden"),window.removeEventListener("wheel",this.scrollListener),window.removeEventListener("keydown",this.scrollListener)}}}),g=i("e4d3"),y=i("21be"),f=i("a293"),b=i("d9bd");const x=Object(d["a"])(o["a"],n["a"],p,g["a"],y["a"],a["a"]);e["a"]=x.extend({name:"v-dialog",directives:{ClickOutside:f["a"]},props:{dark:Boolean,disabled:Boolean,fullscreen:Boolean,light:Boolean,maxWidth:[String,Number],noClickAnimation:Boolean,origin:{type:String,default:"center center"},persistent:Boolean,retainFocus:{type:Boolean,default:!0},scrollable:Boolean,transition:{type:[String,Boolean],default:"dialog-transition"},width:[String,Number]},data(){return{activatedBy:null,animate:!1,animateTimeout:-1,stackMinZIndex:200,previousActiveElement:null}},computed:{classes(){return{[("v-dialog "+this.contentClass).trim()]:!0,"v-dialog--active":this.isActive,"v-dialog--persistent":this.persistent,"v-dialog--fullscreen":this.fullscreen,"v-dialog--scrollable":this.scrollable,"v-dialog--animated":this.animate}},contentClasses(){return{"v-dialog__content":!0,"v-dialog__content--active":this.isActive}},hasActivator(){return Boolean(!!this.$slots.activator||!!this.$scopedSlots.activator)}},watch:{isActive(t){var e;t?(this.show(),this.hideScroll()):(this.removeOverlay(),this.unbind(),null===(e=this.previousActiveElement)||void 0===e||e.focus())},fullscreen(t){this.isActive&&(t?(this.hideScroll(),this.removeOverlay(!1)):(this.showScroll(),this.genOverlay()))}},created(){this.$attrs.hasOwnProperty("full-width")&&Object(b["e"])("full-width",this)},beforeMount(){this.$nextTick(()=>{this.isBooted=this.isActive,this.isActive&&this.show()})},beforeDestroy(){"undefined"!==typeof window&&this.unbind()},methods:{animateClick(){this.animate=!1,this.$nextTick(()=>{this.animate=!0,window.clearTimeout(this.animateTimeout),this.animateTimeout=window.setTimeout(()=>this.animate=!1,150)})},closeConditional(t){const e=t.target;return!(this._isDestroyed||!this.isActive||this.$refs.content.contains(e)||this.overlay&&e&&!this.overlay.$el.contains(e))&&this.activeZIndex>=this.getMaxZIndex()},hideScroll(){this.fullscreen?document.documentElement.classList.add("overflow-y-hidden"):p.options.methods.hideScroll.call(this)},show(){!this.fullscreen&&!this.hideOverlay&&this.genOverlay(),this.$nextTick(()=>{this.$nextTick(()=>{var t,e;(null===(t=this.$refs.dialog)||void 0===t?void 0:t.contains(document.activeElement))||(this.previousActiveElement=document.activeElement,null===(e=this.$refs.dialog)||void 0===e||e.focus()),this.bind()})})},bind(){window.addEventListener("focusin",this.onFocusin)},unbind(){window.removeEventListener("focusin",this.onFocusin)},onClickOutside(t){this.$emit("click:outside",t),this.persistent?this.noClickAnimation||this.animateClick():this.isActive=!1},onKeydown(t){if(t.keyCode===m["x"].esc&&!this.getOpenDependents().length)if(this.persistent)this.noClickAnimation||this.animateClick();else{this.isActive=!1;const t=this.getActivator();this.$nextTick(()=>t&&t.focus())}this.$emit("keydown",t)},onFocusin(t){if(!t||!this.retainFocus)return;const e=t.target;if(e&&this.$refs.dialog&&![document,this.$refs.dialog].includes(e)&&!this.$refs.dialog.contains(e)&&this.activeZIndex>=this.getMaxZIndex()&&!this.getOpenDependentElements().some(t=>t.contains(e))){const t=this.$refs.dialog.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'),e=[...t].find(t=>!t.hasAttribute("disabled"));e&&e.focus()}},genContent(){return this.showLazyContent(()=>[this.$createElement(s["a"],{props:{root:!0,light:this.light,dark:this.dark}},[this.$createElement("div",{class:this.contentClasses,attrs:{role:"dialog","aria-modal":this.hideOverlay?void 0:"true",...this.getScopeIdAttrs()},on:{keydown:this.onKeydown},style:{zIndex:this.activeZIndex},ref:"content"},[this.genTransition()])])])},genTransition(){const t=this.genInnerContent();return this.transition?this.$createElement("transition",{props:{name:this.transition,origin:this.origin,appear:!0}},[t]):t},genInnerContent(){const t={class:this.classes,attrs:{tabindex:this.isActive?0:void 0},ref:"dialog",directives:[{name:"click-outside",value:{handler:this.onClickOutside,closeConditional:this.closeConditional,include:this.getOpenDependentElements}},{name:"show",value:this.isActive}],style:{transformOrigin:this.origin}};return this.fullscreen||(t.style={...t.style,maxWidth:Object(m["h"])(this.maxWidth),width:Object(m["h"])(this.width)}),this.$createElement("div",t,this.getContentSlot())}},render(t){return t("div",{staticClass:"v-dialog__container",class:{"v-dialog__container--attached":""===this.attach||!0===this.attach||"attach"===this.attach}},[this.genActivator(),this.genContent()])}})},"368e":function(t,e,i){},"3c93":function(t,e,i){},"98ab":function(t,e,i){"use strict";var s=i("62ad"),a=i("a523"),o=i("132d"),n=i("0fd9"),l=i("2db4"),r=function(){var t=this,e=t._self._c;return e(a["a"],[e(l["a"],{attrs:{color:t.color,top:"",dense:"",shaped:"",absolute:"","multi-line":""},model:{value:t.snackbarA,callback:function(e){t.snackbarA=e},expression:"snackbarA"}},[e(n["a"],[e(s["a"],{attrs:{cols:"1"}},[e(o["a"],[t._v(" "+t._s(t.icon)+" ")])],1),e(s["a"],{attrs:{cols:"10"}},[t._v(" "+t._s(t.text)+" ")])],1)],1)],1)},c=[],d={name:"",props:["text","icon","color","snackbarA","rigth","left"],data:()=>({show:!1}),mounted(){this.show=snackbarA},methods:{}},h=d,u=i("2877"),m=Object(u["a"])(h,r,c,!1,null,null,null);e["a"]=m.exports},a844:function(t,e,i){"use strict";i("1681");var s=i("8654"),a=i("58df");const o=Object(a["a"])(s["a"]);e["a"]=o.extend({name:"v-textarea",props:{autoGrow:Boolean,noResize:Boolean,rowHeight:{type:[Number,String],default:24,validator:t=>!isNaN(parseFloat(t))},rows:{type:[Number,String],default:5,validator:t=>!isNaN(parseInt(t,10))}},computed:{classes(){return{"v-textarea":!0,"v-textarea--auto-grow":this.autoGrow,"v-textarea--no-resize":this.noResizeHandle,...s["a"].options.computed.classes.call(this)}},noResizeHandle(){return this.noResize||this.autoGrow}},watch:{autoGrow(t){this.$nextTick(()=>{var e;t?this.calculateInputHeight():null===(e=this.$refs.input)||void 0===e||e.style.removeProperty("height")})},lazyValue(){this.autoGrow&&this.$nextTick(this.calculateInputHeight)},rowHeight(){this.autoGrow&&this.$nextTick(this.calculateInputHeight)}},mounted(){setTimeout(()=>{this.autoGrow&&this.calculateInputHeight()},0)},methods:{calculateInputHeight(){const t=this.$refs.input;if(!t)return;t.style.height="0";const e=t.scrollHeight,i=parseInt(this.rows,10)*parseFloat(this.rowHeight);t.style.height=Math.max(i,e)+"px"},genInput(){const t=s["a"].options.methods.genInput.call(this);return t.tag="textarea",delete t.data.attrs.type,t.data.attrs.rows=this.rows,t},onInput(t){s["a"].options.methods.onInput.call(this,t),this.autoGrow&&this.calculateInputHeight()},onKeyDown(t){this.isFocused&&13===t.keyCode&&t.stopPropagation(),this.$emit("keydown",t)}}})},b1bd:function(t,e,i){"use strict";i.r(e);var s=i("8336"),a=i("b0af"),o=i("99d9"),n=i("62ad"),l=i("a523"),r=i("8fea"),c=i("169a"),d=i("ce7e"),h=i("132d"),u=i("0fd9"),m=i("b974"),v=i("2fa4"),p=i("8654"),g=i("a844"),y=i("71d9"),f=i("2a7f"),b=function(){var t=this,e=t._self._c;return e("div",{staticClass:"py-1 px-1"},[[e(r["a"],{staticClass:"elevation-1",attrs:{headers:t.headers,items:t.desserts,"sort-by":"id desc","multi-sort":"",dense:"","items-per-page":100,"headers-length":100,height:"600","fixed-header":""},scopedSlots:t._u([{key:"top",fn:function(){return[e(y["a"],{attrs:{flat:""}},[e(f["a"],[t._v("Category's")]),e(d["a"],{staticClass:"mx-4",attrs:{inset:"",vertical:""}}),e(v["a"]),e(c["a"],{attrs:{"max-width":"500px"},scopedSlots:t._u([{key:"activator",fn:function({on:i,attrs:a}){return[e(s["a"],t._g(t._b({staticClass:"mx-2",attrs:{fab:"",dark:"",small:"",color:"blue"}},"v-btn",a,!1),i),[e(h["a"],{attrs:{dark:""}},[t._v(" mdi-plus ")])],1)]}}]),model:{value:t.dialog,callback:function(e){t.dialog=e},expression:"dialog"}},[e(a["a"],{attrs:{dark:""}},[e(o["c"],[e("span",{staticClass:"text-h5"},[t._v(t._s(t.formTitle))])]),e(o["b"],[e(l["a"],[e(u["a"],[e(n["a"],{attrs:{cols:"12",sm:"12",md:"12"}},[e(p["a"],{attrs:{label:"Category"},model:{value:t.editedItem.CategoryName,callback:function(e){t.$set(t.editedItem,"CategoryName",e)},expression:"editedItem.CategoryName"}})],1),e(n["a"],{attrs:{cols:"12",sm:"12",md:"12"}},[e(g["a"],{attrs:{label:"Description"},model:{value:t.editedItem.Description,callback:function(e){t.$set(t.editedItem,"Description",e)},expression:"editedItem.Description"}})],1),"New Item"!=t.formTitle?e(n["a"],{attrs:{cols:"12",sm:"12",md:"12"}},[e(m["a"],{attrs:{label:"Status",id:"editedItem.Status.id",items:t.StatusList,"item-text":"StatusNames"},model:{value:t.editedItem.Status.StatusNames,callback:function(e){t.$set(t.editedItem.Status,"StatusNames",e)},expression:"editedItem.Status.StatusNames"}})],1):t._e()],1)],1)],1),e(o["a"],[e(v["a"]),e(s["a"],{attrs:{color:"blue darken-1",text:""},on:{click:t.close}},[t._v(" Cancel ")]),e(s["a"],{attrs:{color:"blue darken-1",text:""},on:{click:t.save}},[t._v(" Save ")])],1)],1)],1),e(c["a"],{attrs:{"max-width":"500px"},model:{value:t.dialogDelete,callback:function(e){t.dialogDelete=e},expression:"dialogDelete"}},[e(a["a"],[e(o["c"],{staticClass:"text-h5"},[t._v("Are you sure you want to delete this item?")]),e(o["a"],[e(v["a"]),e(s["a"],{attrs:{color:"blue darken-1",text:""},on:{click:t.closeDelete}},[t._v("Cancel")]),e(s["a"],{attrs:{color:"blue darken-1",text:""},on:{click:t.deleteItemConfirm}},[t._v("OK")]),e(v["a"])],1)],1)],1)],1)]},proxy:!0},{key:"item.actions",fn:function({item:i}){return[e(h["a"],{staticClass:"mr-2",attrs:{small:""},on:{click:function(e){return t.editItem(i)}}},[t._v(" mdi-pencil ")]),e(h["a"],{attrs:{small:""},on:{click:function(e){return t.deleteItem(i)}}},[t._v(" mdi-delete ")])]}},{key:"no-data",fn:function(){return[e(s["a"],{attrs:{color:"primary"},on:{click:t.initialize}},[t._v(" Reset ")])]},proxy:!0}])})],e("Alert",{attrs:{color:"red",text:t.textAX,icon:"mdi-shield-remove-outline",snackbarA:t.snackbarAX}})],2)},x=[],w=i("bc3a"),k=i.n(w),I=i("98ab"),C={components:{Alert:I["a"]},name:"",data:()=>({breadcrumbsI:[{text:"Dashboard",disabled:!1,to:"/"},{text:"Inventory",disabled:!1,to:"/"},{text:"Category",disabled:!0,to:""}],dialog:!1,dialogDelete:!1,headers:[{text:"Branch",value:"Branch.NameBranch",class:"white--text black darken-3 "},{text:"Category",value:"CategoryName",class:"white--text black darken-3 "},{text:"Description",value:"Description",class:"white--text black darken-3 "},{text:"Status",value:"Status.StatusNames",class:"white--text black darken-3 "},{text:"Actions",value:"actions",sortable:!1,class:"white--text black darken-3 "}],desserts:[],editedIndex:-1,editedItem:{id:0,owner:[],date_time_m:"",date_time_c:"",date_create:"",date_change:"",Status:[],Branch:[],CategoryName:"",Description:""},defaultItem:{id:0,owner:[],date_time_m:"",date_time_c:"",date_create:"",date_change:"",Status:[],Branch:[],CategoryName:"",Description:""},StatusList:[],snackbarAX:!1,textAX:""}),computed:{formTitle(){return-1===this.editedIndex?"New Item":"Edit Item"}},watch:{dialog(t){t||this.close()},dialogDelete(t){t||this.closeDelete()}},created(){this.initialize()},mounted(){this.$store.commit("bartitlex",""),this.$store.commit("breadcrumbsx",this.breadcrumbsI),this.STList()},methods:{async STList(){var t=this;await axios.get("/api/Status").then((function(e){let i=0;for(i in e.data)e.data[i].is_material&&t.StatusList.push(e.data[i])})).catch((function(t){console.log(t)}))},async initialize(){var t=this;t.snackbarAX=!1,t.textAX="",await k.a.get("/api/Category").then((function(e){"Your time has expired :"===e.data.Alert||"Your profile not has permissions to run queries"===e.data.Alert?(t.snackbarAX=!0,t.textAX=e.data.Alert+" "+e.data.Date):t.desserts=e.data})).catch((function(t){console.log(t)}))},editItem(t){this.editedIndex=this.desserts.indexOf(t),this.editedItem=Object.assign({},t),this.dialog=!0},deleteItem(t){this.editedIndex=this.desserts.indexOf(t),this.editedItem=Object.assign({},t),this.dialogDelete=!0},async deleteItemConfirm(){var t=this;await axios.post("/apitux/CategoryAxios",{editedItem:t.editedItem,action:"Delete"}).then((function(e){t.desserts.splice(t.editedIndex,1),t.closeDelete()})).catch((function(t){console.log(t)}))},close(){this.dialog=!1,this.$nextTick(()=>{this.editedItem=Object.assign({},this.defaultItem),this.editedIndex=-1})},closeDelete(){this.dialogDelete=!1,this.$nextTick(()=>{this.editedItem=Object.assign({},this.defaultItem),this.editedIndex=-1})},async save(){var t=this;this.editedIndex>-1?await axios.post("/apitux/CategoryAxios",{editedItem:t.editedItem,action:"Edit"}).then((function(e){Object.assign(t.desserts[t.editedIndex],t.editedItem)})).catch((function(t){console.log(t)})):await axios.post("/apitux/CategoryAxios",{editedItem:t.editedItem,action:"Create"}).then((function(e){axios.get("/api/Category/?search="+e.data.id).then((function(e){console.log(e.data),t.editedItem=e.data[0],t.desserts.push(t.editedItem),t.desserts.sort(compareValues("id","desc"))}))})).catch((function(t){console.log(t)})),this.close()}}},S=C,A=i("2877"),_=Object(A["a"])(S,b,x,!1,null,null,null);e["default"]=_.exports}}]);
//# sourceMappingURL=Category.67114708.js.map