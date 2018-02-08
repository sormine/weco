<?php 
use Roots\Sage\Menu;
?>

<?php if(is_home()): ?>
<div id="element" class="introLoading"></div>
<?php endif; ?>
    
  <nav id="sidr" style="overflow-x: visible;">
		<a id="mainmenu" class="menu-button" href="#"></a>
		<div class="row inmenu">
			<div class="col-md-9"></div>
			<div class="col-md-3">
				<form role="search" method="get" class="search-form" action="<?php echo home_url( '/' ); ?>">
					<input type="search" class="search-field" placeholder="Search…" value="" name="s" title="Search for:" />
					<input type="submit" value="a" class="iconSearch">
				</form>
			</div>
		</div>
		<div class="row rowmenu">
			<?= Menu\primary_menu(); ?>
		</div><!-- /.row .rowmenu -->
		<div class="row rowmenu">
			<div class="col">
				<a href="/fr" class="lang">FR</a>
				<div class="clearfix"></div>
				<a href="<?= get_field('weco_linkedin', 107); ?>" class="linkedin" target="_blank"><i class="zmdi zmdi-linkedin"></i></a>
				<div class="clearfix"></div>
				<a href="tel:<?= get_field('weco_phone_number', 107); ?>" class="info"><?= get_field('weco_phone_number', 107); ?></a><a href="mailto:<?= get_field('weco_e-mail', 107); ?>" class="info"><?= get_field('weco_e-mail', 107); ?></a>
			</div>	
		</div>
  </nav>

  <div id="overlay"></div>
	
	<header class="d-flex align-items-center">	
		<div class="col-md-8 col-sm-6 p-0">
			<div>
				<?= Menu\header_menu(); ?>
			</div>
		</div>
		<div class="col-md-4 col-sm-6">
			<div class="row tools">
				<div class="col-md-4 col-sm-6 d-flex align-items-center justify-content-end">
					<a href="#"><i class="zmdi zmdi-phone-msg"></i></a>
					<a href="#"><i class="zmdi zmdi-lock-open"></i></a>
					<a href="#">
						<i class="zmdi zmdi-globe"></i>
						<i class="zmdi zmdi-chevron-down red" style="display: none;"></i>
					</a>
				</div>	
				<div class="col-md-8 col-sm-6">
					<form role="search" method="get" class="search-form" action="<?php echo home_url( '/' ); ?>">						
						<input type="search" class="search-field" placeholder="Search…" value="" name="s" title="Search for:" />
						<input type="submit" value="a" class="iconSearch">
					</form>
				</div>
			</div>
		</div>		
	</header>