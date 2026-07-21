particlesJS("particles-js", {

    particles: {

        number: {
            value: 80,
            density: {
                enable: true,
                value_area: 900
            }
        },

        color: {
            value: "#ff1e1e"
        },

        shape: {
            type: "circle"
        },

        opacity: {
            value: 0.6,
            random: true
        },

        size: {
    value: 6,
    random: true
},

        line_linked: {
            enable: true,
            distance: 170,
            color: "#ff1e1e",
            opacity: 0.5,
            width: 1
        },

        move: {
            enable: true,
            speed: 2,
            direction: "none",
            random: false,
            straight: false,
            out_mode: "out",
            bounce: false
        }

    },

    interactivity: {

        detect_on: "canvas",

        events: {

            onhover: {
                enable: true,
                mode: "grab"
            },

            onclick: {
                enable: true,
                mode: "push"
            },

            resize: true

        },

        modes: {

            grab: {
                distance: 180,
                line_linked: {
                    opacity: 0.8
                }
            },

            push: {
                particles_nb: 4
            }

        }

    },

    retina_detect: true

});