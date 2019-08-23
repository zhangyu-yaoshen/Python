class Player {
    constructor() {
        if (Player.instance)
            return Player.instance;
        return this.getInstance(...arguments);
    }
    getInstance() {
        let instance = new PlayerCreator(...arguments);
        Player.instance = instance;
        return instance;
    }
}
class Musics {
    constructor() {
        this.songs = [{
            id: 1,
            title: 'Driving Home for Christmas',
            singer: 'Campsite Dream',
            songUrl: './songs/jq22.mp3',
            imageUrl: './images/songs/c.jpg'
        }, {
            id: 2,
            title: '认真的雪',
            singer: '薛之谦',
            songUrl: './songs/认真的雪 - 薛之谦.mp3',
            imageUrl: './images/songs/renzhendexue.jpg'
        }, {
            id: 3,
            title: '演员',
            singer: '薛之谦',
            songUrl: './songs/演员 - 薛之谦.mp3',
            imageUrl: './images/songs/yanyuan.jpg'
        }]
    }
    getSongByNum(index) {
        return this.songs[index];
    }
}
class PlayerCreator {
    constructor() {
        this.audio = document.querySelector('.music-player__audio')
        this.audio.volume = 0.8;
        this.util = new Util();
        this.musics = new Musics();
        this.song_index = 0;
        this.loop_mode = 0;
        this.song_list = $('.music__list_content');
        this.render_doms = {
            title: $('.music__info--title'),
            singer: $('.music__info--singer'),
            image: $('.music-player__image img'),
            blur: $('.music-player__blur')
        }
        this.ban_dom = {
            control__btn: $('.control__volume--icon')
        }
        this.render_time = {
            now: $('.nowTime'),
            total: $('.totalTime')
        }
        this.disc = {
            image: $('.music-player__image'),
            pointer: $('.music-player__pointer')
        };
        this.init();
    }
    init() {
        this.renderSongList();
        this.renderSongStyle();
        this.bindEventListener();
    }
    renderSongList() {
        let _str = '';
        this.musics.songs.forEach((song,i)=>{
            _str += `<li class="music__list__item">${song.title}</li>`
        }
        );
        this.song_list.html(_str);
    }
    renderSongStyle() {
        let {title, singer, songUrl, imageUrl} = this.musics.getSongByNum(this.song_index);
        this.audio.src = songUrl;
        this.render_doms.title.html(title);
        this.render_doms.singer.html(singer);
        this.render_doms.image.prop('src', imageUrl);
        this.render_doms.blur.css('background-image', 'url("' + imageUrl + '")');
        this.song_list.find('.music__list__item').eq(this.song_index).addClass('play').siblings().removeClass('play');
    }
    bindEventListener() {
        this.$play = new Btns('.player-control__btn--play',{
            click: this.handlePlayAndPause.bind(this)
        });
        this.$prev = new Btns('.player-control__btn--prev',{
            click: this.changeSong.bind(this, 'prev')
        });
        this.$next = new Btns('.player-control__btn--next',{
            click: this.changeSong.bind(this, 'next')
        });
        this.$mode = new Btns('.player-control__btn--mode',{
            click: this.changePlayMode.bind(this)
        });
        this.$ban = new Btns('.control__volume--icon',{
            click: this.banNotes.bind(this)
        })
        this.song_list.on('click', 'li', (e)=>{
            let index = $(e.target).index();
            this.changeSong(index);
        }
        )
        new Progress('.control__volume--progress',{
            min: 0,
            max: 1,
            value: this.audio.volume,
            handler: (value)=>{
                this.audio.volume = value;
            }
        })
        this.audio.oncanplay = ()=>{
            if (this.progress) {
                this.progress.max = this.audio.duration;
                this.render_time.total.html(this.util.formatTime(this.audio.duration));
                return false;
            }
            ;this.progress = new Progress('.player__song--progress',{
                min: 0,
                max: this.audio.duration,
                value: 0,
                handler: (value)=>{
                    this.audio.currentTime = value;
                }
            })
            this.render_time.total.html(this.util.formatTime(this.audio.duration));
        }
        this.audio.ontimeupdate = ()=>{
            this.progress.setValue(this.audio.currentTime);
            this.render_time.now.html(this.util.formatTime(this.audio.currentTime));
        }
        this.audio.onended = ()=>{
            this.changeSong('next');
            this.audio.play();
        }
    }
    handlePlayAndPause() {
        let _o_i = this.$play.$el.find('i');
        if (this.audio.paused) {
            this.audio.play();
            _o_i.removeClass('icon-play').addClass('icon-pause');
            this.disc.image.addClass('play');
            this.disc.pointer.addClass('play')
        } else {
            this.audio.pause();
            _o_i.addClass('icon-play').removeClass('icon-pause');
            this.disc.image.removeClass('play');
            this.disc.pointer.removeClass('play');
        }
    }
    changePlayMode() {
        this.loop_mode++;
        if (this.loop_mode > 2)
            this.loop_mode = 0;
        this.renderPlayMode();
    }
    renderPlayMode() {
        let _classess = ['loop', 'random', 'single'];
        let _o_i = this.$mode.$el.find('i');
        _o_i.prop('class', 'iconfont icon-' + _classess[this.loop_mode])
    }
    changeSongIndex(type) {
        if (typeof type === 'number') {
            this.song_index = type;
        } else {
            if (this.loop_mode === 0) {
                this.song_index += type === 'next' ? 1 : -1;
                if (this.song_index > this.musics.songs.length - 1)
                    this.song_index = 0;
                if (this.song_index < 0)
                    this.song_index = this.musics.songs.length - 1;
            } else if (this.loop_mode === 1) {
                let _length = this.musics.songs.length;
                let _random = Math.floor(Math.random() * _length);
                for (let i = 0; i < 10000; i++) {
                    if (this.song_index == _random) {
                        _random = Math.floor(Math.random() * _length);
                    } else {
                        this.song_index = _random;
                        break;
                    }
                }
            } else if (this.loop_mode === 2) {
                this.song_index = this.song_index;
            }
        }
    }
    songTime() {
        let totalMinute = parseInt(this.audio.duration / 60) < 10 ? "0" + parseInt(this.audio.duration / 60) : parseInt(this.audio.duration / 60);
        let totalSecond = parseInt(this.audio.duration % 60) < 10 ? "0" + parseInt(this.audio.duration % 60) : parseInt(this.audio.duration % 60);
        $('.totalTime').text(totalMinute + ':' + totalSecond);
    }
    changeSong(type) {
        this.changeSongIndex(type);
        let _is_pause = this.audio.paused;
        this.renderSongStyle();
        if (!_is_pause)
            this.audio.play();
    }
    banNotes() {
        let _o_i = this.$ban.$el.find("i");
        if (this.audio.muted == true) {
            this.audio.muted = false;
            _o_i.removeClass('icon-muted').addClass('icon-volume');
        } else {
            this.audio.muted = true;
            _o_i.removeClass('icon-volume').addClass('icon-muted');
        }
    }
}
class Progress {
    constructor(selector, options) {
        $.extend(this, options);
        this.$el = $(selector);
        this.width = this.$el.width();
        this.init();
    }
    init() {
        this.renderBackAndPointer();
        this.drag();
        this.value;
        this.changeDOMStyle(this.width * this.value);
    }
    renderBackAndPointer() {
        this.$back = $('<div class="back">');
        this.$pointer = $('<div class="pointer">');
        this.$el.append(this.$back);
        this.$el.append(this.$pointer);
    }
    setValue(value) {
        let _distance = this.width * value / (this.max - this.min);
        this.changeDOMStyle(_distance);
    }
    drag() {
        let ele = this.$pointer;
        let father = this.$el;
        let flag = false;
        ele.mousedown((e)=>{
            flag = true;
            let mousePos = {
                x: e.offsetX
            }
            $(document).mousemove((e)=>{
                if (flag === true) {
                    let _left = e.clientX - father.offset().left - mousePos.x;
                    let _distance = Math.max(0, Math.min(_left, father.outerWidth(false) - ele.outerWidth(false)))
                    let _ratio = _distance / father.outerWidth(false);
                    let _value = _ratio * (this.max - this.min);
                    this.changeDOMStyle(_distance);
                    this.handler(_value);
                }
            }
            )
        }
        )
        $(document).mouseup(()=>{
            flag = false;
        }
        )
    }
    bindEvents() {
        this.$el.click((e)=>{
            let _x = e.offsetX;
            let _ratio = _x / this.width;
            let _value = _ratio * (this.max - this.min);
            this.changeDOMStyle(_x);
            this.handler(_value);
        }
        )
    }
    changeDOMStyle(distance) {
        this.$back.width(distance + 7 == 7 ? 0 : distance + 7);
        this.$pointer.css('left', distance + 'px');
    }
}
class Btns {
    constructor(selector, handlers) {
        this.$el = $(selector);
        this.bindEvents(handlers);
    }
    bindEvents(handlers) {
        for (const event in handlers) {
            if (handlers.hasOwnProperty(event)) {
                this.$el.on(event, handlers[event]);
            }
        }
    }
}
new Player();
