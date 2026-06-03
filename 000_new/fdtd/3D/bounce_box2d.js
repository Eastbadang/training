function eventWindowLoaded() {
   canvasApp();
}

function canvasSupport () {
   return Modernizr.canvas;
}

function canvasApp() {
	if (!canvasSupport()) {
    return;
	}
	function  drawScreen () {
    world.Step(1 / 60, 10, 10);
    world.DrawDebugData();
    world.ClearForces()
  }
   	theCanvas = document.getElementById('canvasOne');
   	context = theCanvas.getContext('2d');
    theCanvas.addEventListener('mousemove',changeGravity,false)

   	var    b2Vec2 = Box2D.Common.Math.b2Vec2
            ,   b2BodyDef = Box2D.Dynamics.b2BodyDef
            ,   b2Body = Box2D.Dynamics.b2Body
            ,   b2FixtureDef = Box2D.Dynamics.b2FixtureDef
            ,   b2World = Box2D.Dynamics.b2World
            ,   b2PolygonShape = Box2D.Collision.Shapes.b2PolygonShape
            ,   b2CircleShape = Box2D.Collision.Shapes.b2CircleShape
            ,   b2DebugDraw = Box2D.Dynamics.b2DebugDraw;

      var world = new b2World(new b2Vec2(0,10),  true);
     	var numBalls = 10;
     	var balls = new Array();
     	for (var i=0; i < numBalls; i++) {
        var ballDef = new b2BodyDef;
        ballDef.type = b2Body.b2_dynamicBody;
        var ypos = (Math.random() * 10)+1;
        var xpos = (Math.random() * 12)+1;
        ballDef.position.Set(xpos, ypos);
        var ballFixture = new b2FixtureDef;
        ballFixture.density = 10.0;
        ballFixture.friction = 0.5;
        ballFixture.restitution = 1;
        ballFixture.shape = new b2PolygonShape;
        ballFixture.shape.SetAsArray([new b2Vec2(-1, 0),new b2Vec2(0, -1),new b2Vec2(1, 0)],3); //triangle shape
        var newBall = world.CreateBody(ballDef)
        newBall.CreateFixture(ballFixture);
        balls.push(newBall);
      }

     	var wallDefs = new Array({x:8.3,y:.03,w:8.3 ,h:.03},      //top
                               {x:8.3,y:13.33,w:8.3 ,h:.03},    //bottom
                               {x:0,y:6.67,w:.03 ,h:6.67},      //left
                               {x:16.7,y:6.67,w:.03 ,h:6.67} ); //right
     	var walls = new Array();
     	for (var i = 0; i <wallDefs.length; i++) {
        var wallDef = new b2BodyDef;
       	wallDef.type = b2Body.b2_staticBody;
      	wallDef.position.Set(wallDefs[i].x, wallDefs[i].y);
      	var newWall = world.CreateBody(wallDef)
      	var wallFixture = new b2FixtureDef;
      	wallFixture.density = 10.0;
      	wallFixture.friction = 0.5;
      	wallFixture.restitution = 0.9;
      	wallFixture.shape = new b2PolygonShape;
      	wallFixture.shape.SetAsBox(wallDefs[i].w, wallDefs[i].h);
      	newWall.CreateFixture(wallFixture);
      	walls.push(newWall);
     	}

   var debugDraw = new b2DebugDraw();
   debugDraw.SetSprite (context);
   debugDraw.SetDrawScale(30);     //define scale
   debugDraw.SetFillAlpha(0.3);    //define transparency
   debugDraw.SetLineThickness(1.0);
   debugDraw.SetFlags(b2DebugDraw.e_shapeBit | b2DebugDraw.e_jointBit);
   world.SetDebugDraw(debugDraw);
   
   function theLoop() {
         window.setTimeout(theLoop, 20);
         drawScreen()
      }

   function changeGravity(event) {
      var x;
      var y;
      if (event.pageX || event.pageY) {
          x = event.pageX;
          y = event.pageY;
      }
      else {
        x = e.clientX + document.body.scrollLeft +
           document.documentElement.scrollLeft;
          y = e.clientY + document.body.scrollTop +
           document.documentElement.scrollTop;
      }
    x -= theCanvas.offsetLeft;
    y -= theCanvas.offsetTop;
    mouseX=x;
    mouseY=y;
    var gravity_vector = new b2Vec2((mouseX-250)/25,(mouseY-250)/25);
    world.SetGravity(gravity_vector)
   }

   theLoop();
}
window.addEventListener('load', eventWindowLoaded, true);