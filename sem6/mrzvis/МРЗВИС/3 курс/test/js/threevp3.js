ThreeVP3 = {
  Animator: function(options) {
    var animator = this;
    this.animes = [];
    this.animate = function() {
      var animes = animator.animes;
      for (var anime in animes) animes[anime].animate();
      requestAnimationFrame( animator.animate );
    }
    this.add = function(anime) {
      this.awake(anime);
      anime.resetAnimator(this);
    }
    this.awake = function(anime) {
      if (this.animes.indexOf(anime) < 0) this.animes.push(anime);
    }
    this.sleep = function(anime) {
      if (this.animes.indexOf(anime) >= 0) this.animes.splice(this.animes.indexOf(anime),1);
    }
    this.remove = function(anime) {
      this.sleep(anime);
      anime.resetAnimator();
    }
    this.clear = function() {
      for (var anime in animes) this.remove(anime);
    }
    for (var anime in options.animes) this.add(options.animes[anime]);
  },

  Visualizer: function(options) {
    if (!this.update) {
      this.update = function() {
        throw 'Abstract method';
      }
    }
    if (!this.animate) {
      this.animate = function() {
        throw 'Abstract method';
      }
    }
    if (!this.resetAnimator) {
      this.resetAnimator = function(animator) {
        throw 'Abstract method';
      }
    }
    if (!this.kill) {
      this.kill = function() {
        var children = this.container.children;
        while(children.length > 0) this.container.removeChild(children[0]);
      }
    }
    if (!this.release) {
      this.release = function() {}
    }
    if (!this.mutate) {
      this.mutate = function(visualizerClass) {
        var options = this.project();
        this.kill();
        visualizerClass.call(this, options);
      }
    }
    if (!this.project) {
      this.project = function() {
        return ThreeVP3.Utils.InheritanceHacks.project.call(this);
      }
    }
    if (!this.inject) {
      this.inject = function(options) {
        ThreeVP3.Utils.InheritanceHacks.inject.call(this, options);
      }
    }
    this.inject(options);
  },
  // //TODO add inject
  // Viewport: function(options) {
  //   ThreeVP3.Visualizer.call(this, options);
  //   this.rendererType = options.rendererType || ThreeVP3.Viewport.DEFAULT_RENDERER_TYPE;
  //   var width = this.width;
  //   var height = this.height;
  //   var viewport = this;
  //   window.onresize = function() {
  //     viewport.width = viewport.container.offsetWidth;
  //     viewport.height = window.innerHeight;
  //     viewport.renderer.setSize(viewport.width, viewport.height);
  //   }
  //   this.initElements = function() {
  //     this.meshes = [];
  //     this.mesh_number = 0;
  //     this.textures = [];
  //     this.texture_number = 0; 
  //     this.view_model_matrix = new THREE.Matrix4();
  //     this.projection_matrix = new THREE.Matrix4(); 
  //   }
  //   this.initScenes = function(options) {
  //     this.currentScene = 0;
  //     this.scenes = [new THREE.Scene(), new THREE.Scene()];
  //     this.cameras = [];
  //     for(var i = 0; i < this.scenes.length; i++) {
  //       var camera = new THREE.PerspectiveCamera(
  //         options.fov, 
  //         this.width / this.height, 
  //         options.near, 
  //         options.far
  //       );
  //       camera.position.x = options.x;
  //       camera.position.y = options.y;
  //       camera.position.z = options.z;
  //       camera.lookAt(this.scenes[i].position);
  //       this.cameras.push(camera);
  //     }
  //     this.initRenderer();
  //     var ambcolor = Math.random() * 0xffffff;
  //     this.ambientLight = [
  //       new THREE.AmbientLight( ambcolor ), 
  //       new THREE.AmbientLight( ambcolor )
  //     ];
  //     this.container.appendChild( this.renderer.domElement );
  //     this.animate();
  //   }
  //   this.initRenderer = function() {
  //     if (this.rendererType == "webgl")
  //       this.renderer = new THREE.WebGLRenderer();
  //     else 
  //       this.renderer = new THREE.CanvasRenderer();
  //     this.renderer.setSize(this.width, this.height);
  //   }
  //   this.animate = function() {
  //     requestAnimationFrame( viewport.animate );
  //     var s = 1 - viewport.currentScene;
  //     viewport.renderer.render( viewport.scenes[s], viewport.cameras[s] );
  //   }
  //   this.project = function() {
  //     var projection = ThreeVP3.Utils.InheritanceHacks.project.call(this, options);
  //     projection.rendererType = this.rendererType;
  //     projection.scenes = {};
  //     projection.scenes.x = this.scenes.x;
  //     projection.scenes.y = this.scenes.y;
  //     projection.scenes.z = this.scenes.z;
  //     projection.scenes.fov = this.scenes.fov;
  //     projection.scenes.near = this.scenes.near;
  //     projection.scenes.far = this.scenes.far;
  //     return projection;
  //   }
  //   //TODO replace mutate with ???
  //   // this.mutate = function(visualizerClass) {
  //   //   var options = this.project();
  //   //   var buffer = {
  //   //     meshes: this.meshes,
  //   //     mesh_number: this.mesh_number,
  //   //     textures: this.textures,
  //   //     texture_number: this.texture_number,
  //   //     view_model_matrix: this.view_model_matrix,
  //   //     projection_matrix: this.projection_matrix,
  //   //     cameras: this.cameras,
  //   //     scenes: this.scenes,
  //   //     ambientLight: this.ambientLight
  //   //   };
  //   //   this.kill();
  //   //   visualizerClass.call(this, options);
  //   //   for(var field in buffer)
  //   //     this[field] = buffer[field];
  //   // }
  //   this.initScenes(options.scenes);
  //   this.initElements();
  // },

  Viewport: function(options) {
    ThreeVP3.Visualizer.call(this, options);
    var viewport = this;
    window.onresize = function() {
      viewport.width = viewport.container.offsetWidth;
      viewport.height = window.innerHeight;
      for (var rendererKey in ThreeVP3.Viewport.RENDERER_CLASSES) {
        if (viewport.renderers[rendererKey])
          viewport.renderers[rendererKey].setSize(viewport.width, viewport.height);
      }
    }
    this.getWindowDimension = function() {
	return {X: viewport.width, Y: viewport.height};
    }
    this.bindDriver = function(f) {
	this.switchLists = f;
    }
    this.initElements = function() {
//	this.data = [	{lists: {clone:[undefined], index: 0, scene: 0}, text: {Mesh: [undefined], MeshIndex:{}}}, 
//			{lists: {clone:[undefined], index: 0, scene: 0}, text: {Mesh: [undefined], MeshIndex:{}}}];
	this.data = [	{lists: [undefined], text: {Mesh: [undefined], MeshIndex:{}}}, 
			{lists: [undefined], text: {Mesh: [undefined], MeshIndex:{}}}];
//	this.meshes = [];
//      this.mesh_number = 0;
//      this.textures = [];
//      this.texture_number = 0; 
//      this.view_model_matrices = [];
//      this.view_model_matrix = new THREE.Matrix4();
//      this.projection_matrix = new THREE.Matrix4(); 
    }
//    this.popViewMatrix = function() {
//      viewport.view_model_matrix = viewport.view_model_matrices.pop();
//    }
//    this.pushViewMatrix = function() {
//      viewport.view_model_matrices.push(viewport.view_model_matrix);
//    }
    this.initScenes = function(options) {
      this.currentScene = this.currentScene || 0;
      this.scenes = [new THREE.Scene(), new THREE.Scene()];
//	this.scenes[0].autoUpdate = false;
//	this.scenes[1].autoUpdate = false;
      this.cameras = [];
      for(var i = 0; i < this.scenes.length; i++) {
        var camera = new THREE.PerspectiveCamera(
          options.fov, 
          this.width / this.height, 
          options.near, 
          options.far
        );
        camera.position.x = options.x;
        camera.position.y = options.y;
        camera.position.z = options.z;
        camera.lookAt(this.scenes[i].position);
        this.cameras.push(camera);
      }
      var ambcolor = options.ambcolor || /*Math.random() * */0xffffff;
      this.ambientLight = [
//        new THREE.AmbientLight( Math.random() * 0xffffff ), 
//        new THREE.AmbientLight( Math.random() * 0xffffff )
        new THREE.AmbientLight( ambcolor ), 
        new THREE.AmbientLight( ambcolor )
      ];
    }
    this.initRenderers = function() {
      this.renderers = [];
      for (var rendererKey in ThreeVP3.Viewport.RENDERER_CLASSES) {
        try {
          this.renderers[rendererKey] = new ThreeVP3.Viewport.RENDERER_CLASSES[rendererKey]._class({antialias:true,alpha:true});
          this.renderers[rendererKey].setSize(this.width, this.height);
          this.renderers[rendererKey].domElement.style.display = "none";
          for(var option in ThreeVP3.Viewport.RENDERER_CLASSES[rendererKey].options) {
            this.renderers[rendererKey][option] = ThreeVP3.Viewport.RENDERER_CLASSES[rendererKey].options[option];
          }
          this.container.appendChild(this.renderers[rendererKey].domElement);
        }
        catch(exception){

        }
      }
    }
    this.reinitRenderer = function() {
      var rendererKey = this.currentRendererKey;
      this.renderers[rendererKey] = new ThreeVP3.Viewport.RENDERER_CLASSES[rendererKey]._class({canvas: this.renderers[rendererKey].domElement});
      this.renderers[rendererKey].setSize(this.width, this.height);
      for(var option in ThreeVP3.Viewport.RENDERER_CLASSES[rendererKey].options) {
        this.renderers[rendererKey][option] = ThreeVP3.Viewport.RENDERER_CLASSES[rendererKey].options[option];
      }
    }
    this.animate = function() {
      var s = 1 - viewport.currentScene, r = viewport.renderers[viewport.currentRendererKey];
      //TODO this is hack. Try to avoid this code.
//      if (statsVisualizer && statsVisualizer.update) 
//	statsVisualizer.update();
//      r.clear(false,true);
      r.render(viewport.scenes[s], viewport.cameras[s]);
      if (r.context && (r.context.getError() !== r.context.NO_ERROR)) {
	brk();
        viewport.release();
        viewport.kill();
	if (viewport.driver) if (viewport.driver.textures) viewport.driver.textures = [undefined];
        viewport.initElements();
        viewport.release();
	viewport.switchLists(viewport.currentScene);
        viewport.initScenes(options.scenes);
        viewport.initRenderers();
        viewport.initRenderer();
        viewport.reinitRenderer();
      }
      //else
      requestAnimationFrame( viewport.animate );
    }
    this.initRenderer = function(rendererKey) {
      brk();
      rendererKey = (rendererKey === undefined)? ThreeVP3.Viewport.CANVAS_RENDERER: rendererKey;
      this.renderers[(this.currentRendererKey === undefined)? rendererKey: this.currentRendererKey].domElement.style.display = "none";
      this.renderers[rendererKey].domElement.style.display = "block";
      this.currentRendererKey = rendererKey;
    }
    this.changeRenderer = function(rendererKey) {
      //this.alpha = undefined;
      //this.color = undefined;      
      if (!this.renderers[rendererKey]) 
        throw "Renderer failed to load"
      this.release();
      //this.kill();
      //if (viewport.driver) if (viewport.driver.textures) viewport.driver.textures = [undefined];
      //this.initScenes(options.scenes);
      //this.initRenderers();
      this.initRenderer(rendererKey);
      //this.reinitRenderer();
    }
    this.kill();
    this.initScenes(options.scenes);
    this.initElements();
    this.initRenderers();
    this.initRenderer(ThreeVP3.Viewport.WEBGL_RENDERER);
    this.animate();
  },

  CanvasThreeViewport: function(options) {
    options.rendererType = "canvas";
    ThreeVP3.Viewport.call(this, options);
  },

  WebGLThreeViewport: function(options) {
    options.rendererType = "webgl";
    ThreeVP3.Viewport.call(this, options);
  },
  
  StatsVisualizer: function(options) {
    ThreeVP3.Visualizer.call(this, options);
    this.stats = new Stats();
    this.container.appendChild( this.stats.domElement );
    this.update = function(options) {
      this.stats.update();
    }
    this.animate = function() {
      this.stats.update();
//      this.stats.render();
    }
    this.resetAnimator = function(animator) {
      this.animator = animator;
    }
  },

  //TODO add override inject call
  ArrayVisualizer: function(options) {
    ThreeVP3.Visualizer.call(this, options);
    this.gradientor = options.gradientor;
    this.project = function() {
      var projection = ThreeVP3.Utils.InheritanceHacks.project.call(this);
      projection.gradientor = this.gradientor;
      return projection;
    }
    this.inject = function(options) {
      ThreeVP3.Utils.InheritanceHacks.inject.call(this, options);
      this.gradientor = options.gradientor;
    }
    this.update = function(object) {
      this.updateArray(object.array);
    }
    if (!this.updateArray) {
      this.updateArray = function(array) {
        throw 'Abstract method';
      }
    }
  },

  CanvasArrayVisualizer: function(options) {
    ThreeVP3.ArrayVisualizer.call(this, options);
    ThreeVP3.CanvasVisualizer.call(this, options);
    this.canvas.width = this.width;
    this.canvas.height = this.height;
    this.updateArray = function(array) {
      var c = this.context;
      var s = this.width;
      var r = array.length/s;
      var h = this.canvas.height;
      for(var i = 0; i < s; i++) {
        c.fillStyle = this.gradientor.getColor(array[(i*r)>>>0]);
        c.fillRect(i, 0, 1, h);
      }
    }
    this.animate = function() {}
    this.resetAnimator = function(animator) {
      this.animator = animator;
    }
  },

  ArrayHistoryVisualizer: function(options) {
    ThreeVP3.ArrayVisualizer.call(this, options);
    this.history = options.history || [];
    this.maxSize = options.maxSize || ThreeVP3.ArrayHistoryVisualizer.DEFAULT_MAX_SIZE;
    this.updateArray = function(array) {
      this.history.unshift(array);
      if (this.history.length > this.maxSize) 
        this.history.pop();
      this.createRow(array);
    }
    if (!this.createRow) {
      this.createRow = function(row) {
        throw 'Abstract method';
      }
    }
  },

  ThreeVisualizer: function(options) {
    ThreeVP3.Visualizer.call(this, options);
    this.rendererType = options.rendererType || ThreeVP3.ThreeVisualizer.DEFAULT_RENDERER_TYPE;

    this.init = function() {
      this.scene = new THREE.Scene();
      this.camera = new THREE.PerspectiveCamera();
      this.scene.add(this.camera);
      this.camera.lookAt(this.scene.position);  
      this.initRenderer(); 
      this.container.appendChild( this.renderer.domElement );
      var light = new THREE.AmbientLight(0xffffff);
      this.scene.add(light);
    }

    this.initRenderer = function() {
      if (this.rendererType == "webgl")
        this.renderer = new THREE.WebGLRenderer({ preserveDrawingBuffer: true });
      else 
        this.renderer = new THREE.CanvasRenderer();
    }

    //TODO project renderer type
    // this.project = function() {
    //   var projection = ThreeVP3.Utils.InheritanceHacks.project.call(this, options);
    //   projection.rendererType = this.rendererType;
    //   return projection;
    // }

    // this.inject = function(options) {
    //   ThreeVP3.Utils.InheritanceHacks.inject.call(this, options);
    //   this.rendererType = options.rendererType;
    // }

    this.init();
  },

  CanvasVisualizer: function(options) {
    ThreeVP3.Visualizer.call(this, options);
    this.canvas = document.createElement('canvas');
    this.container.appendChild(this.canvas);
    this.context = this.canvas.getContext(options.type || ThreeVP3.CanvasVisualizer.DEFAULT_TYPE);
  },

  CanvasArrayHistoryVisualizer: function(options) {
    ThreeVP3.ArrayHistoryVisualizer.call(this, options);
    ThreeVP3.CanvasVisualizer.call(this, options);
    this.canvas.width = this.width;
    this.container.width = this.width;
    this.canvas.height = 1;
    this.container.height = 1;
    this.createRow = function(row) {
      var ratio = row.length/this.width;
      var image = this.context.getImageData(0, 0, this.canvas.width, this.canvas.height);
      if (this.canvas.height < this.maxSize) 
        this.canvas.height += 1;
      this.context.putImageData(image, 0, 1);
      for(var i = 0; i < this.width; i++) {
        this.context.fillStyle = this.gradientor.getColor(row[(i*ratio)>>>0]);
        this.context.fillRect(i, 0, 1, 1);
      }
    }
    this.animate = function() {}
    this.resetAnimator = function(animator) {
      this.animator = animator;
    }
  },

  ThreeArrayVisualizer: function(options) {
    ThreeVP3.ArrayVisualizer.call(this, options);
    ThreeVP3.ThreeVisualizer.call(this, options);

    this.initCamera = function() {
      this.camera.fov = 90;
      this.camera.aspect = this.width/this.height;
      this.camera.near = this.height/2;
      this.camera.far = this.camera.near + 1;
      this.camera.updateProjectionMatrix();
      this.camera.position.set(this.width/2, this.height/2, this.camera.near);
    }

    this.initMesh = function() {
      var geometry = new THREE.Geometry();
      var h = this.height;
      geometry.vertices.push( new THREE.Vector3(0, 0, 0) );
      geometry.vertices.push( new THREE.Vector3(0, h, 0) );
      for(var i = 1; i <= this.width; i++) {
        geometry.vertices.push( new THREE.Vector3(i, 0, 0) );
        geometry.vertices.push( new THREE.Vector3(i, h, 0) );
        var tmp = i + i;
        if (THREE.REVISION > 59) {
          geometry.faces.push(new THREE.Face3( tmp - 1, tmp - 2, tmp + 1));
          geometry.faces.push(new THREE.Face3( tmp + 1, tmp - 2, tmp));
	}	
	else geometry.faces.push(new THREE.Face4( tmp - 1, tmp - 2, tmp, tmp + 1));
      }

      var material = new THREE.MeshBasicMaterial( { color: 0xffffff, vertexColors: THREE.FaceColors } );
      this.mesh = new THREE.Mesh( geometry, material );
      this.scene.add(this.mesh);
    }

    this.initScene = function() {
      this.renderer.setSize(this.width, this.height);
      this.initCamera();
      this.initMesh();
    }

    this.initScene();

    if (THREE.REVISION > 59) {
      this.updateArray = function(array) {
        var geometry = this.mesh.geometry;
        var faces = geometry.faces;
        var gradientor = this.gradientor;
        var ratio = array.length/faces.length;
        for ( var i = 0; i < faces.length; i +=2 ) {
	  var c = gradientor.getColor(array[(i*ratio)>>>0]);
          faces[i].color.set(c);
          faces[i+1].color.set(c);
        }
        geometry.colorsNeedUpdate = true;
      }
    }
    else {
      this.updateArray = function(array) {
        var geometry = this.mesh.geometry;
        var faces = geometry.faces;
        var gradientor = this.gradientor;
        var ratio = array.length/faces.length;
        for ( var i = 0; i < faces.length; i ++ ) {
          faces[i].color.set(gradientor.getColor(array[(i*ratio)>>>0]));
        }
        geometry.colorsNeedUpdate = true;
      }
    }

    this.animate = function() {
      this.renderer.render(this.scene, this.camera); 
    }

    this.resetAnimator = function(animator) {
      this.animator = animator;
    }
  },

  CanvasThreeArrayVisualizer: function(options) {
    options.rendererType = "canvas";
    ThreeVP3.ThreeArrayVisualizer.call(this, options);
  },

  WebGLThreeArrayVisualizer: function(options) {
    options.rendererType = "webgl";
    ThreeVP3.ThreeArrayVisualizer.call(this, options);
  },

  ThreeArrayHistoryVisualizer: function(options) {
    ThreeVP3.ArrayHistoryVisualizer.call(this, options);
    ThreeVP3.ThreeVisualizer.call(this, options);
    this.height = this.maxSize;
    this.currentSize = 0;
    this.systems = [];

    this.initCamera = function() {
      this.camera.fov = 90;
      //this.camera.aspect = this.width/2;
      this.camera.aspect = this.width;
      //this.camera.near = 1;
      this.camera.near = 1/2;
      this.camera.far = this.camera.near + 2;
      this.camera.updateProjectionMatrix();
      //this.camera.position.set(this.width/2 - 1/2, -this.height/2, this.camera.near);
      this.camera.position.set(this.width/2 - 1/2, 1/2, this.camera.near);
    }

    this.initScene = function() {
      //this.renderer.setSize(this.width, this.height);
      //this.renderer.setSize(this.width, 2);
      this.renderer.setSize(this.width, 1);
      this.initCamera();
      this.vertices = [];
      for(var i = 0; i < this.width; i++)
        this.vertices.push( new THREE.Vector3(i, 0, 0) );
      this.material = new THREE.ParticleBasicMaterial( { color: 0xffffff, size: 1, vertexColors: THREE.VertexColors, sizeAttenuation: false } );
    }

    this.initScene();

    this.createRow = function(row) {
      var array = row;
      var gradientor = this.gradientor;
      var ratio = array.length/this.width;
      if (this.currentSize < this.height) {
        var camera = this.camera;
        var geometry = new THREE.Geometry();
        var colors = geometry.colors = [];
        geometry.vertices = this.vertices;
        for(var i = 0; i < this.width; i++) {
          colors.push( new THREE.Color(gradientor.getColor(array[(i*ratio)>>>0])) );
        }
        var system = new THREE.ParticleSystem( geometry, this.material );
        system.position.y = this.currentSize++;
        camera.aspect = this.width/this.currentSize;
        camera.near = this.currentSize/2;
        camera.far = camera.near + 2;
        camera.updateProjectionMatrix();
        camera.position.set(this.width/2 - 1/2, this.currentSize-this.currentSize/2, camera.near);
        this.renderer.setSize(this.width, this.currentSize);
        this.scene.add(system);
        this.systems.push(system);
        this.animate(); 
      }
      else {
        var system = this.systems[this.currentSize-this.height];
        var geometry = system.geometry;
        var colors = geometry.colors;
        for(var i = 0; i < this.width; i++)
          colors[i].set(gradientor.getColor(array[(i*ratio)>>>0]));
        system.position.y = this.currentSize++;
        this.camera.position.y++;
        geometry.colorsNeedUpdate = true;
         
        if (this.currentSize == this.height+this.height) {
          this.currentSize -= this.height;
          this.camera.position.y -= this.height;
          for(var i = 0; i < this.currentSize; i++)
            this.systems[i].position.y = i; 
        }
      }
    }
    this.animate = function() {
      this.renderer.render(this.scene, this.camera); 
    }

    this.resetAnimator = function(animator) {
      this.animator = animator;
    }
  },

  //Do not use because of particle system canvas conflict!
  CanvasThreeArrayHistoryVisualizer: function(options) {
    options.rendererType = "canvas";
    ThreeVP3.ThreeArrayHistoryVisualizer.call(this, options);
  },

  WebGLThreeArrayHistoryVisualizer: function(options) {
    options.rendererType = "webgl";
    ThreeVP3.ThreeArrayHistoryVisualizer.call(this, options);
  },

  Utils: {
    //TODO add real inheritance and method overriding
    InheritanceHacks: {
      project: function() {
        return {
          container: this.container,
          width: this.width,
          height: this.height
        };
      },
      inject: function(options) {
        this.container = options.container;
        this.width = options.width || ThreeVP3.Visualizer.DEFAULT_WIDTH;
        this.height = options.height || ThreeVP3.Visualizer.DEFAULT_HEIGHT
      }
    },
    WebGLDetector: function() {
      var f = true; 
      try {
//        var canvas = document.createElement( 'ThreeVP3WebGLDetectorCanvas' );
//        return !!( window.WebGLRenderingContext && (
//          canvas.getContext( 'webgl' ) ||
//          canvas.getContext( 'experimental-webgl' ) )
//        );
          var c = document.createElement( 'ThreeVP3WebGLDetectorContainer' );
          var testVisualizer = new ThreeVP3.ThreeArrayVisualizer({container: c, width: ThreeVP3.Visualizer.DEFAULT_WIDTH, gradientor: {}, rendererType: "webgl"});
          testVisualizer.kill();

      } catch ( exception ) { f = false; }
      return f;
    },
    Gradientor: function(json) {
      this.colormap = {};
      this.valuemap = [];
      this.values = json.values.slice();
      this.colors = json.colors.slice();
      this.addGradient = function(startColor, finalColor, startPoint, finalPoint) {
        var l = 0;
        var u = this.values.length;
        var s = (u-l) >> 1;
        while (this.values[s] != startPoint && s > l) {
          if (this.values[s] > startPoint) u = s;
          else l = s;
          s = l + ((u-l) >> 1);
        }
        l = s;
        u = this.values.length;
        var f = u - ((u-l) >> 1);
        while (this.values[f] != finalPoint && u > f) {
          if (this.values[f] < finalPoint) l = f;
          else u = f;
          f = u - ((u-l) >> 1);
        }
        var preStartColor;
        if (this.values[s]+1 < startPoint) {
          preStartColor = ThreeVP3.Utils.recountColor(startPoint-1,this.colors[s],this.colors[s+1],this.values[s],this.values[s+1]);
        }
        else if (this.values[s] == startPoint && s > 0) {
          preStartColor = ThreeVP3.Utils.recountColor(startPoint-1,this.colors[s-1],this.colors[s],this.values[s-1],this.values[s]);
        }

        if (this.values[f] > finalPoint+1) {
          var value = finalPoint+1;
          var color = ThreeVP3.Utils.recountColor(value,this.colors[f-1],this.colors[f],this.values[f-1],this.values[f]);
          this.values.splice(f,0,value);
          this.colors.splice(f,0,color);
        }
        else if (this.values[f] == finalPoint && f+1 < this.values.length) {
          var value = finalPoint+1;
          var color = ThreeVP3.Utils.recountColor(value,this.colors[f],this.colors[f+1],this.values[f],this.values[f+1]);
          this.values.splice(f,1);
          this.colors.splice(f,1);
          if (value < this.values[f]) {
            this.values.splice(f,0,value);
            this.colors.splice(f,0,color);
          }
        }
        else if (this.values[f] == finalPoint) this.colors[this.colors.length - 1] = finalColor;
        if (f+1 < this.values.length || this.values[f] > finalPoint) if (finalPoint > startPoint) {
          this.values.splice(f,0,finalPoint);
          this.colors.splice(f,0,finalColor);
        }

        if (this.values[s]+1 < startPoint) {
          var value = startPoint-1;
          var color = preStartColor;
          s++;
          this.values.splice(s,0,value);
          this.colors.splice(s,0,color);
          s++;
          f++;
        }
        else if (this.values[s] == startPoint && s > 0) {
          var value = startPoint-1;
          var color = preStartColor;
          this.values.splice(s,1);
          this.colors.splice(s,1);
          f--;
          if (value > this.values[s-1]) {
            this.values.splice(s,0,value);
            this.colors.splice(s,0,color);
            s++;
            f++;
          }
        }
        else if (this.values[s] == startPoint) this.colors[0] = startColor;
        else if (this.values[s] < startPoint) s++;
        if (s > 0) {
          this.values.splice(s,0,startPoint);
          this.colors.splice(s,0,startColor);
          f++;
        }
        s++;
        if (f > s) this.values.splice(s,f-s);
        if (f > s) this.colors.splice(s,f-s);

        this.colormap = {};
        this.valuemap = [];
      }
      this.getColor = function(value) {
        if (!this.colormap[value]) {
          var values = this.values;
          var l = 0;
          var u = values.length-1;
          var s = u - ((u-l) >> 1);
          while ((values[s] != value) && (u > s)) {
            if (values[s] < value) l = s;
            else u = s;
            s = u - ((u-l) >> 1);
          }
          if (this.valuemap.length == ThreeVP3.Utils.Gradientor.MAP_SIZE) {
            delete this.colormap[this.valuemap[0]];
            this.valuemap.shift();
          }
          this.colormap[value] = ThreeVP3.Utils.recountColor(value,this.colors[l],this.colors[s],values[l],values[s]);
          this.valuemap.push(value);
        }
        return this.colormap[value];
      }
    },
    recountColor: function(number, startColor, finishColor, startPoint, finishPoint) {
      var percent = (number - startPoint)/(finishPoint - startPoint);
      var apercent = 1-percent;
/*      var color2 = startColor.substring(1);
      var color1 = finishColor.substring(1);
      var r = Math.floor(parseInt(color1.substring(0,2), 16) * percent + parseInt(color2.substring(0,2), 16) * apercent);
      var g = Math.floor(parseInt(color1.substring(2,4), 16) * percent + parseInt(color2.substring(2,4), 16) * apercent);
      var b = Math.floor(parseInt(color1.substring(4,6), 16) * percent + parseInt(color2.substring(4,6), 16) * apercent);
*/      var color1 = parseInt(finishColor.substring(1),16);
      var color2 = parseInt(startColor.substring(1),16);
      var r = ((color1&0xFF0000)*percent+(color2&0xFF0000)*apercent)>>>16;
      var g = ((color1&0x00FF00)*percent+(color2&0x00FF00)*apercent)>>>8;
      var b = ((color1&0x0000FF)*percent+(color2&0x0000FF)*apercent)>>>0;
      var h = ThreeVP3.Utils.hex;
      return "#" + h(r) + h(g) + h(b);
    },
    hex: function(x) {
      x = x.toString(16);
      return (x.length < 2)? "0"+x: x;
    }
  }
}

ThreeVP3.Visualizer.DEFAULT_WIDTH = 1000;
ThreeVP3.Visualizer.DEFAULT_HEIGHT = 32;
ThreeVP3.CanvasVisualizer.DEFAULT_TYPE = '2d';
ThreeVP3.Viewport.DEFAULT_RENDERER_TYPE = "canvas";
ThreeVP3.ThreeVisualizer.DEFAULT_RENDERER_TYPE = "canvas";
ThreeVP3.ArrayHistoryVisualizer.DEFAULT_MAX_SIZE = 1000;
ThreeVP3.Utils.Gradientor.MAP_SIZE = ThreeVP3.Visualizer.DEFAULT_WIDTH;

ThreeVP3.Viewport.WEBGL_RENDERER = 0;
ThreeVP3.Viewport.CANVAS_RENDERER = 1;
ThreeVP3.Viewport.RENDERER_CLASSES = [
	{
		_class: THREE.WebGLRenderer,
		options: {
			autoClear: false,
			autoClearDepth: false,
			autoClearStencil: false
		}
	}, 
	{
		_class: THREE.CanvasRenderer,
		options: {
		}
	}
]