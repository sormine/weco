<?php
use Roots\Sage\Menu;
?>

<aside id="leftSidebar">
	<ul>

		<?php 
			$args = array(
		    'post_type' => 'left_sidebar',
		    'order'     => 'ASC',
		    'orderby'   => 'meta_value_num',
		    'metakey'   => 'page_order'
		  );

		  $sidebar_links = new WP_Query($args);

		  if($sidebar_links->have_posts()):
		    $count_links = 1;

		    while($sidebar_links->have_posts()): $sidebar_links->the_post();
		      echo '<li>';
		      echo '<a href="'.get_field('page')->guid.'" class="b-service-'.$count_links.'">';
		      echo '<span class="slider-tooltip"><span></span>'.get_field('page')->post_title.'</span>';
		      echo get_field('icon_svg');
		      echo '</a>';
		      echo '</li>';
		      $count_links++;
		    endwhile;
		  endif;
		  wp_reset_postdata();
		?>

	</ul>
</aside>