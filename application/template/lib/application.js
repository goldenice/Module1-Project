(function($, block) {
	block.fn.wordcloud = function(config) {
		var options = $.extend({
			filter_function : function(cat,val,max) { return true; },
			weight_function : function(cat,val,max) { return val; },
			options : {}
		}, config);

		var addword = function(label, value) {
			alert(label);
		}		

		var $container = $(this.$element);

		this.actions = {
			'set': function(e, message) {
				alert(e + message);
			},
			'add': function(e, message) {
				alert(e + message);
			}
		}

		return this.$element;
	}
})(jQuery, block);
