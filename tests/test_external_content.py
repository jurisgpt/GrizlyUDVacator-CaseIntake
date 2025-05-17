import streamlit as st
from bs4 import BeautifulSoup
import pytest
import re

# Define the HTML content once for all tests
markdown = """
<div class="component-container">
    <div class="loader">Loading&hellip;</div>
    
    <div class="iframe-wrapper" style="display: none;">
        <iframe
            src="https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform?embedded=true"
            onload="this.style.display='block'; document.querySelector('.loader').style.display='none';"
            onerror="handleFrameError(this)"
            style="width: 640px; height: 1544px; border: none;"
            title="Tenant Relief Evaluation Form"
            aria-label="Tenant Relief Evaluation Form"
            role="application"
        ></iframe>
        
        <div id="iframe-fallback" style="display: none;">
            <div class="error-message">
                <h4>⚠️ Content Failed to Load</h4>
                <p>Please check your internet connection or try again later.</p>
                <p><a href="https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform" 
                      rel="noopener noreferrer" 
                      target="_blank">Open the form directly</a></p>
            </div>
        </div>
    </div>
</div>

<script>
function handleFrameError(frame) {
    const container = frame.closest('.component-container');
    container.querySelector('.loader').style.display = 'none';
    container.querySelector('#iframe-fallback').style.display = 'block';
    console.error('Iframe failed to load:', frame.src);
}
</script>

<noscript>
    <div class="noscript-warning">
        <h4>⚠️ JavaScript Required</h4>
        <p>This feature requires JavaScript to be enabled.</p>
        <p><a href="https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform" 
              rel="noopener noreferrer" 
              target="_blank">Open the form directly</a></p>
    </div>
</noscript>
"""

# Pre-parse the HTML once for all tests
soup = BeautifulSoup(markdown, 'html.parser')

def test_external_content_structure():
    """Test the overall structure of the external content component"""
    iframe = soup.find('iframe')
    assert iframe is not None
    
    # Test iframe attributes
    assert iframe.get('onload') == "this.style.display='block'; document.querySelector('.loader').style.display='none';"
    assert iframe.get('onerror') == "handleFrameError(this)"
    assert iframe.get('style') == "width: 640px; height: 1544px; border: none;"
    assert iframe.get('title') == "Tenant Relief Evaluation Form"
    assert iframe.get('aria-label') == "Tenant Relief Evaluation Form"
    assert iframe.get('role') == "application"
    
    # Test fallback content
    fallback = soup.find('div', {'id': 'iframe-fallback'})
    assert fallback is not None
    assert fallback.get('style') == "display: none;"
    
    error_message = fallback.find('div', {'class': 'error-message'})
    assert error_message is not None
    
    h4 = error_message.find('h4')
    assert h4 is not None
    assert h4.text == "⚠️ Content Failed to Load"
    
    p1 = error_message.find_all('p')[0]
    assert p1 is not None
    assert p1.text == "Please check your internet connection or try again later."
    
    p2 = error_message.find_all('p')[1]
    assert p2 is not None
    
    link = p2.find('a')
    assert link is not None
    assert link.get('href') == "https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform"
    assert link.get('rel') == ['noopener', 'noreferrer']
    assert link.get('target') == "_blank"
    assert link.text == "Open the form directly"

    container = soup.find('div', class_='component-container')
    assert container is not None
    
    # Verify loader
    loader = container.find('div', class_='loader')
    assert loader is not None
    assert loader.text.strip() == 'Loading&hellip;'
    
    # Verify iframe wrapper
    wrapper = container.find('div', class_='iframe-wrapper')
    assert wrapper is not None
    assert wrapper.get('style') == 'display: none;'
    
    # Verify iframe
    iframe = wrapper.iframe
    assert iframe is not None
    assert iframe.get('src') == 'https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform?embedded=true'
    
    # Verify fallback content
    fallback = container.find('div', id='iframe-fallback')
    assert fallback is not None
    assert fallback.get('style') == 'display: none;'
    assert fallback.text.strip() == 'Failed to load content. Please try refreshing the page.'
    
    # Verify noscript fallback
    noscript = container.noscript
    assert noscript is not None
    assert noscript.text.strip() == 'JavaScript is required to view this content. Please enable JavaScript in your browser settings.'

def test_iframe_attributes():
    """Test iframe attributes and their values"""
    
    iframe = soup.iframe
    assert iframe is not None
    
    required_attrs = {
        'src': re.compile(r'https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform'),
        'style': 'width: 640px; height: 1544px; border: none;',
        'title': 'Tenant Relief Evaluation Form',
        'aria-label': 'Tenant Relief Evaluation Form',
        'role': 'application'
    }
    
    for attr, expected in required_attrs.items():
        assert attr in iframe.attrs
        value = iframe[attr]
        if isinstance(expected, re.Pattern):
            assert expected.match(value)
        else:
            assert value == expected

def test_error_handling():
    """Test error handling elements"""
    
    # Verify error fallback
    fallback = soup.find('div', id='iframe-fallback')
    assert fallback is not None
    assert fallback.get('style') == 'display: none;'
    
    # Verify error message structure
    error_msg = fallback.find('div', class_='error-message')
    assert error_msg is not None
    assert error_msg.h4 is not None
    assert error_msg.p is not None
    assert error_msg.a is not None

def test_noscript_handling():
    """Test noscript fallback"""
    
    noscript = soup.noscript
    assert noscript is not None
    
    warning = noscript.find('div', class_='noscript-warning')
    assert warning is not None
    assert warning.h4 is not None
    assert warning.p is not None
    assert warning.a is not None

def test_css_styles():
    """Test CSS styles are properly included"""
    assert '<style>' in markdown
    
    # Verify specific styles exist
    assert '.component-container' in markdown
    assert '.loader' in markdown
    assert '.error-message' in markdown
    assert '.noscript-warning' in markdown

if __name__ == '__main__':
    pytest.main([__file__])
