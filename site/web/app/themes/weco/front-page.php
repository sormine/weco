<section id="homeSlider">
	<div class="textIntro homeslider d-flex justify-content-center">
		<h2><?= get_field('slider_title', 5); ?></h2>
		<span class="line-slider"></span>
		<h3><?= get_field('slider_subtitle', 5); ?></h3>
	</div>
	<div class="homeslider">

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

		    	echo '<figure id="service-'.$count_links.'" class="homeslider active d-flex justify-content-center" style="background: url('.get_field('background_image').'); background-size: cover;">
						</figure>';
		 
		      $count_links++;
		    endwhile;
		  endif;
		  wp_reset_postdata();
		?>

	</div>
</section>

<section id="featuredProducts">
	<div class="row">

		<?php var_dump(get_field('home_highlighted_products')); ?>

		<div class="col product">
			<a href="#">
				<figure><img src="/app/uploads/2018/02/PCB-connectors.png" alt="example product" /></figure>
				<h4>PCB Connectors</h4>
				<span class="b-product"><span>explore</span></span>
			</a>
		</div>

		<div class="col product">
			<a href="#">
				<figure><img src="/app/uploads/2018/02/PCB-connectors.png" alt="example product" /></figure>
				<h4>PCB Connectors</h4>
				<span class="b-product"><span>explore</span></span>
			</a>
		</div>
		<div class="col product">
			<a href="#">
				<figure><img src="/app/uploads/2018/02/PCB-connectors.png" alt="example product" /></figure>
				<h4>PCB Connectors</h4>
				<span class="b-product"><span>explore</span></span>
			</a>
		</div>
		<div class="col product">
			<a href="#">
				<figure><img src="/app/uploads/2018/02/PCB-connectors.png" alt="example product" /></figure>
				<h4>PCB Connectors</h4>
				<span class="b-product"><span>explore</span></span>
			</a>
		</div>
		<div class="col product">
			<a href="#">
				<figure><img src="/app/uploads/2018/02/PCB-connectors.png" alt="example product" /></figure>
				<h4>PCB Connectors</h4>
				<span class="b-product"><span>explore</span></span>
			</a>
		</div>
	</div>
</section>

<section id="whoAreWe">
	<div class="container">
		<div class="row d-flex align-items-center">
			<div class="col-12 bigTitle p-0 m-0"><?= get_field('who_are_we_title', 5); ?></div>
			<div class="col-lg-4 waw-logo">
				<img src="<?= get_template_directory_uri(); ?>/dist/images/logo-weco.svg" class="logo" alt="Weco Connectors" />
			</div>
			<div class="col-lg-8 grayBox">
				<?= get_field('who_are_we_content', 5); ?>
				<p><a href="#">EN SAVOIR PLUS</a>
			</div>
		</div>
	</div>
</section>

<section id="video">
	<a href="<?= get_field('video_link', 5); ?>" data-fancybox class="b-video d-flex align-items-center">
		<span class="playicon"><i class="zmdi zmdi-youtube-play"></i></span>
		<img src="<?= get_field('video_image_background', 5); ?>" width="100%" alt="" />
	</a>
</section>

<section id="news">
	<div class="container">
		<div class="row">
			<div class="col">
				<h2><span></span>News</h2>
			</div>
		</div>
	</div>
	<div class="newsSlider">
	  <div class="newsSlide grow">
		<div class="date">02 / 10 / 2017</div>
		<div class="newsInfos">
			<p>WECO est FIER d’annoncer l’arrivée dans ses rangs de Monsieur Paul A. Simmons</p>
			<p><a href="#" class="b-more">More</a></p>
			<span class="redline"></span>
		</div>
		<img src="http://weco.test/app/uploads/2018/02/news1.jpg" alt="news1 background" />
	  </div>
	  <div class="newsSlide grow">
		<div class="date">02 / 10 / 2017</div>
		<div class="newsInfos">
			<p>WECO est FIER d’annoncer l’arrivée dans ses rangs de Monsieur Paul A. Simmons</p>
			<p><a href="#" class="b-more">More</a></p>
			<span class="redline"></span>
		</div>
		<img src="http://weco.test/app/uploads/2018/02/news1.jpg" alt="news1 background" />
	  </div>
	  <div class="newsSlide grow">
		<div class="date">02 / 10 / 2017</div>
		<div class="newsInfos">
			<p>WECO est FIER d’annoncer l’arrivée dans ses rangs de Monsieur Paul A. Simmons</p>
			<p><a href="#" class="b-more">More</a></p>
			<span class="redline"></span>
		</div>
		<img src="http://weco.test/app/uploads/2018/02/news1.jpg" alt="news1 background" />
	  </div>
	  <div class="newsSlide grow">
		<div class="date">02 / 10 / 2017</div>
		<div class="newsInfos">
			<p>WECO est FIER d’annoncer l’arrivée dans ses rangs de Monsieur Paul A. Simmons</p>
			<p><a href="#" class="b-more">More</a></p>
			<span class="redline"></span>
		</div>
		<img src="http://weco.test/app/uploads/2018/02/news1.jpg" alt="news1 background" />
	  </div>
	  <div class="newsSlide grow">
		<div class="date">02 / 10 / 2017</div>
		<div class="newsInfos">
			<p>WECO est FIER d’annoncer l’arrivée dans ses rangs de Monsieur Paul A. Simmons</p>
			<p><a href="#" class="b-more">More</a></p>
			<span class="redline"></span>
		</div>
		<img src="http://weco.test/app/uploads/2018/02/news1.jpg" alt="news1 background" />
	  </div>
	  <div class="newsSlide grow">
		<div class="date">02 / 10 / 2017</div>
		<div class="newsInfos">
			<p>WECO est FIER d’annoncer l’arrivée dans ses rangs de Monsieur Paul A. Simmons</p>
			<p><a href="#" class="b-more">More</a></p>
			<span class="redline"></span>
		</div>
		<img src="http://weco.test/app/uploads/2018/02/news1.jpg" alt="news1 background" />
	  </div>
	  <div class="newsSlide grow">
		<div class="date">02 / 10 / 2017</div>
		<div class="newsInfos">
			<p>WECO est FIER d’annoncer l’arrivée dans ses rangs de Monsieur Paul A. Simmons</p>
			<p><a href="#" class="b-more">More</a></p>
			<span class="redline"></span>
		</div>
		<img src="http://weco.test/app/uploads/2018/02/news1.jpg" alt="news1 background" />
	  </div>
	  <div class="newsSlide grow">
		<div class="date">02 / 10 / 2017</div>
		<div class="newsInfos">
			<p>WECO est FIER d’annoncer l’arrivée dans ses rangs de Monsieur Paul A. Simmons</p>
			<p><a href="#" class="b-more">More</a></p>
			<span class="redline"></span>
		</div>
		<img src="http://weco.test/app/uploads/2018/02/news1.jpg" alt="news1 background" />
	  </div>
	  <div class="newsSlide grow">
		<div class="date">02 / 10 / 2017</div>
		<div class="newsInfos">
			<p>WECO est FIER d’annoncer l’arrivée dans ses rangs de Monsieur Paul A. Simmons</p>
			<p><a href="#" class="b-more">More</a></p>
			<span class="redline"></span>
		</div>
		<img src="http://weco.test/app/uploads/2018/02/news1.jpg" alt="news1 background" />
	  </div>
	  <div class="newsSlide grow">
		<div class="date">02 / 10 / 2017</div>
		<div class="newsInfos">
			<p>WECO est FIER d’annoncer l’arrivée dans ses rangs de Monsieur Paul A. Simmons</p>
			<p><a href="#" class="b-more">More</a></p>
			<span class="redline"></span>
		</div>
		<img src="http://weco.test/app/uploads/2018/02/news1.jpg" alt="news1 background" />
	  </div>
	</div>
</section>