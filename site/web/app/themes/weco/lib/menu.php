<?php 

namespace Roots\Sage\Menu;

function primary_menu() {
  $output = '';
  $output_single_parent = '';
  $col_single_parent = false;

  $parent_pages = get_pages(array('parent' => 0, 'sort_column' => 'menu_order', 'exclude' => array(5))); // remove home page

  foreach($parent_pages as $parent_page) {

    $children_pages = get_pages(array('child_of' => $parent_page->ID, 'sort_column' => 'menu_order'));

   
    if(count($children_pages)) {
      // parent pages with children pages

      $output .= '<div class="col">';
      $output .= '<ul>';
      $output .= '<li>';
      $output .= '<span><a href="'.$parent_page->guid.'">'.$parent_page->post_title.'</a></span>';
      $output_children = '';

      if(count($children_pages)) {
        $output_children .= '<ul>';
        
        foreach($children_pages as $children_page) {
          $output_children .= '<li>';
          $output_children .= '<a href="'.$children_page->guid.'">'.$children_page->post_title.'</a>';
          $output_children .= '</li>';
        }
        $output_children .= '</ul>';
      }

      $output .= $output_children;
      $output .= '</li>';
      $output .= '</ul>';
      $output .= '</div>';
    } else {
      // parent pages without children pages

      if(!$col_single_parent) {
        $output_single_parent .= '<div class="col">';
        $output_single_parent .= '<ul>';
        $output_single_parent .= '<li>';
        $col_single_parent = true;
      }

      $output_single_parent .= '<span><a href="'.$parent_page->guid.'">'.$parent_page->post_title.'</a></span>';
    }
  }

  $output_single_parent .= '</li>';
  $output_single_parent .= '</ul>';
  $output_single_parent .= '</div>';

  $output .= $output_single_parent;

  return $output;
}

function header_menu() {
    $first_parent_page = true;
    $output = '';
    $output .= '<ul class="nav d-flex align-items-center">';
    $output .= '<a class="navbar-brand" href="'.get_home_url().'">';
    $output .= '<img src="'.get_template_directory_uri().'/dist/images/logo-weco.svg" class="logo" alt="Weco Connectors" />';
    $output .= '</a>';

    $header_pages = wp_get_nav_menu_items('header-navigation');

    foreach($header_pages as $header_page) {
      
      if($header_page->post_parent == 0) { // parent pages
        if(!$first_parent_page) {
          $output .= '</div>';
          $output .= '</li>';
        }
        $first_parent_page = false;
        $output .= '<li class="nav-item dropdown top-nav">';
        $output .= '<a class="nav-link dropdown-toggle" data-toggle="dropdown" href="'.$header_page->url.'" role="button" aria-haspopup="true" aria-expanded="false">';
        $output .= $header_page->title;
        $output .= '</a>';
        $output .= '<div class="dropdown-menu">';
      } else { // children pages
        $output .= '<a class="dropdown-item" href="'.$header_page->url.'">'.$header_page->title.'</a>';
      }
    }

    $output .= '</div>';
    $output .= '</li>';
    $output .= '</ul>';

    return $output;
}