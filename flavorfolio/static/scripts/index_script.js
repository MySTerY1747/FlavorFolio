$(document).ready(function () {
  $("#load-more").on("click", function () {
    const button = $(this);
    const targetUrl = button.data("ajax-target");

    button.text("Loading...");
    button.prop("disabled", true);

    $.ajax({
      url: targetUrl,
      type: 'GET',
      success: function (data) {
        button.before(data);

        if (data.trim() === "") {
          button.hide();
          return;
        }

        const currentNum = parseInt(button.data("ajax-target").match(/\d+$/)[0]);
        const newNum = currentNum + 5;
        button.data("ajax-target", button.data("ajax-target").replace(/\d+$/, newNum));

        button.text("Load More");
        button.prop("disabled", false);

        $(".recipe-list li").slice(-5).hide().fadeIn(800);
      },
      error: function () {
        button.text("Error loading recipes");
        setTimeout(function () {
          button.text("Load More");
          button.prop("disabled", false);
        }, 2000);
      }
    });
  });

  $(".recipe-list li").each(function () {
    $(this).on({
      mouseenter: function () {
        $(this).css({
          'transform': 'scale(1.03)',
          'transition': 'transform 0.3s ease',
          'box-shadow': '0 4px 8px rgba(0,0,0,0.2)',
          'background-color': 'rgba(255, 248, 220, 0.7)'  // Light cornsilk background
        });
      },
      mouseleave: function () {
        $(this).css({
          'transform': 'scale(1)',
          'transition': 'transform 0.3s ease',
          'box-shadow': 'none',
          'background-color': 'inherit'
        });
      }
    });
  });

  $(document).on({
    mouseenter: function () {
      $(this).css({
        'transform': 'scale(1.03)',
        'transition': 'transform 0.3s ease',
        'box-shadow': '0 4px 8px rgba(0,0,0,0.2)',
        'background-color': 'rgba(255, 248, 220, 0.7)'
      });
    },
    mouseleave: function () {
      $(this).css({
        'transform': 'scale(1)',
        'transition': 'transform 0.3s ease',
        'box-shadow': 'none',
        'background-color': 'inherit'
      });
    }
  }, ".recipe-list li");

  $(".tags li").on({
    mouseenter: function () {
      $(this).css({
        'transform': 'translateY(-3px)',
        'transition': 'transform 0.2s ease',
        'font-weight': 'bold'
      });
    },
    mouseleave: function () {
      $(this).css({
        'transform': 'translateY(0)',
        'transition': 'transform 0.2s ease',
        'font-weight': 'normal'
      });
    }
  });

  // Apply the same hover effect to dynamically loaded tags
  $(document).on({
    mouseenter: function () {
      $(this).css({
        'transform': 'translateY(-3px)',
        'transition': 'transform 0.2s ease',
        'font-weight': 'bold'
      });
    },
    mouseleave: function () {
      $(this).css({
        'transform': 'translateY(0)',
        'transition': 'transform 0.2s ease',
        'font-weight': 'normal'
      });
    }
  }, ".tags li");

  $(".recipe-list li").each(function (index) {
    $(this).css('opacity', '0');
    setTimeout(() => {
      $(this).animate({
        opacity: 1
      }, 500);
    }, index * 150); // Stagger the animations
  });

  $(".recipe-image").on({
    mouseenter: function () {
      $(this).css({
        'transform': 'scale(1.1)',
        'transition': 'transform 0.3s ease',
        'cursor': 'pointer'
      });
    },
    mouseleave: function () {
      $(this).css({
        'transform': 'scale(1)',
        'transition': 'transform 0.3s ease'
      });
    }
  });

  $(document).on({
    mouseenter: function () {
      $(this).css({
        'transform': 'scale(1.1)',
        'transition': 'transform 0.3s ease',
        'cursor': 'pointer'
      });
    },
    mouseleave: function () {
      $(this).css({
        'transform': 'scale(1)',
        'transition': 'transform 0.3s ease'
      });
    }
  }, ".recipe-image");
});
